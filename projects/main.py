
from datetime import date


# ============================================================
# DATA STORAGE
# ============================================================

borrowers = []
loans = []
repayments = []


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def generate_id(prefix, records):
    """Generate a unique ID based on the number of existing records."""
    return f"{prefix}{len(records) + 1:03d}"


def get_non_empty_input(message):
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Error: This field cannot be empty.")


def get_positive_integer(message):
    """Get a positive integer from the user."""
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Error: Enter a number greater than zero.")

        except ValueError:
            print("Error: Please enter a valid integer.")


def get_interest_rate():
    """Get a valid interest rate."""
    while True:
        try:
            rate = float(input("Enter interest rate (%): "))

            if 0 < rate <= 100:
                return rate

            print("Interest rate must be greater than 0 and at most 100.")

        except ValueError:
            print("Error: Enter a valid interest rate.")


def format_money(amount):
    return f"MWK {amount:,.2f}"


def find_borrower(borrower_id):
    """Find a borrower using their ID."""
    for borrower in borrowers:
        if borrower["id"] == borrower_id:
            return borrower

    return None


def find_loan(loan_id):
    """Find a loan using its ID."""
    for loan in loans:
        if loan["id"] == loan_id:
            return loan

    return None


# ============================================================
# 1. BORROWER MANAGEMENT
# ============================================================

def register_borrower():
    print("\n========== REGISTER BORROWER ==========")

    name = get_non_empty_input("Full name: ")
    phone = get_non_empty_input("Phone number: ")
    monthly_income = get_positive_integer("Monthly income (MWK): ")

    print("\nEmployment status:")
    print("1. EMPLOYED")
    print("2. SELF_EMPLOYED")
    print("3. UNEMPLOYED")

    while True:
        choice = input("Choose employment status: ").strip()

        employment_options = {
            "1": "EMPLOYED",
            "2": "SELF_EMPLOYED",
            "3": "UNEMPLOYED"
        }

        if choice in employment_options:
            employment_status = employment_options[choice]
            break

        print("Invalid choice. Try again.")

    borrower = {
        "id": generate_id("BRW", borrowers),
        "name": name,
        "phone": phone,
        "monthly_income": monthly_income,
        "employment_status": employment_status
    }

    borrowers.append(borrower)

    print("\nBorrower registered successfully!")
    print(f"Borrower ID: {borrower['id']}")

    return borrower


def list_borrowers():
    print("\n========== REGISTERED BORROWERS ==========")

    if not borrowers:
        print("No borrowers registered.")
        return

    for borrower in borrowers:
        print("-" * 45)
        print(f"ID: {borrower['id']}")
        print(f"Name: {borrower['name']}")
        print(f"Phone: {borrower['phone']}")
        print(f"Monthly income: {format_money(borrower['monthly_income'])}")
        print(f"Employment: {borrower['employment_status']}")


def search_borrower():
    print("\n========== SEARCH BORROWER ==========")

    borrower_id = get_non_empty_input("Enter borrower ID: ").upper()

    borrower = find_borrower(borrower_id)

    if borrower is None:
        print("Borrower not found.")
        return

    print("\nBorrower details:")
    print(f"ID: {borrower['id']}")
    print(f"Name: {borrower['name']}")
    print(f"Phone: {borrower['phone']}")
    print(f"Monthly income: {format_money(borrower['monthly_income'])}")
    print(f"Employment: {borrower['employment_status']}")


# ============================================================
# 2. LOAN ELIGIBILITY
# ============================================================

def evaluate_eligibility(borrower, requested_amount):
    """
    Check whether a borrower qualifies for a loan.

    Educational rules:
    - Borrower must have positive monthly income.
    - Loan amount cannot exceed 3 times monthly income.
    - Borrower cannot have another outstanding loan.
    """

    if borrower["monthly_income"] <= 0:
        return False, "Borrower has no valid monthly income."

    maximum_loan = borrower["monthly_income"] * 3

    if requested_amount > maximum_loan:
        return False, (
            f"Requested amount exceeds the maximum eligible amount "
            f"of {format_money(maximum_loan)}."
        )

    outstanding_loans = [
        loan for loan in loans
        if loan["borrower_id"] == borrower["id"]
        and loan["status"] == "ACTIVE"
        and loan["balance"] > 0
    ]

    if outstanding_loans:
        return False, "Borrower already has an outstanding loan."

    return True, "Borrower qualifies for this loan."


# ============================================================
# 3. LOAN APPLICATIONS
# ============================================================

def apply_for_loan():
    print("\n========== LOAN APPLICATION ==========")

    if not borrowers:
        print("Register a borrower before applying for a loan.")
        return

    borrower_id = get_non_empty_input("Enter borrower ID: ").upper()

    borrower = find_borrower(borrower_id)

    if borrower is None:
        print("Borrower does not exist.")
        return

    print(f"\nBorrower: {borrower['name']}")
    print(f"Monthly income: {format_money(borrower['monthly_income'])}")

    amount = get_positive_integer("Loan amount (MWK): ")
    interest_rate = get_interest_rate()
    duration = get_positive_integer("Repayment duration (months): ")

    eligible, reason = evaluate_eligibility(borrower, amount)

    if not eligible:
        print("\nLoan application cannot proceed.")
        print(f"Reason: {reason}")
        return

    interest = round(amount * interest_rate / 100)
    total_payable = amount + interest

    loan = {
        "id": generate_id("LN", loans),
        "borrower_id": borrower_id,
        "amount": amount,
        "interest_rate": interest_rate,
        "duration_months": duration,
        "interest": interest,
        "total_payable": total_payable,
        "amount_paid": 0,
        "balance": 0,
        "status": "PENDING",
        "rejection_reason": None,
        "application_date": date.today().isoformat(),
        "disbursement_date": None
    }

    loans.append(loan)

    print("\nLoan application submitted successfully!")
    print(f"Loan ID: {loan['id']}")
    print(f"Principal: {format_money(amount)}")
    print(f"Interest: {format_money(interest)}")
    print(f"Total payable: {format_money(total_payable)}")
    print(f"Status: {loan['status']}")


def list_loans():
    print("\n========== ALL LOANS ==========")

    if not loans:
        print("No loan applications found.")
        return

    for loan in loans:
        borrower = find_borrower(loan["borrower_id"])
        borrower_name = borrower["name"] if borrower else "Unknown"

        print("-" * 50)
        print(f"Loan ID: {loan['id']}")
        print(f"Borrower: {borrower_name}")
        print(f"Principal: {format_money(loan['amount'])}")
        print(f"Total payable: {format_money(loan['total_payable'])}")
        print(f"Amount paid: {format_money(loan['amount_paid'])}")
        print(f"Balance: {format_money(loan['balance'])}")
        print(f"Duration: {loan['duration_months']} months")
        print(f"Status: {loan['status']}")

        if loan["rejection_reason"]:
            print(f"Rejection reason: {loan['rejection_reason']}")


def list_pending_loans():
    print("\n========== PENDING APPLICATIONS ==========")

    pending_loans = [
        loan for loan in loans
        if loan["status"] == "PENDING"
    ]

    if not pending_loans:
        print("No pending applications.")
        return

    for loan in pending_loans:
        borrower = find_borrower(loan["borrower_id"])

        print("-" * 40)
        print(f"Loan ID: {loan['id']}")
        print(f"Borrower: {borrower['name']}")
        print(f"Amount: {format_money(loan['amount'])}")
        print(f"Status: {loan['status']}")


# ============================================================
# 4. LOAN APPROVAL AND REJECTION
# ============================================================

def approve_loan():
    print("\n========== APPROVE LOAN ==========")

    loan_id = get_non_empty_input("Enter loan ID: ").upper()

    loan = find_loan(loan_id)

    if loan is None:
        print("Loan not found.")
        return

    if loan["status"] != "PENDING":
        print("Only pending applications can be approved.")
        return

    loan["status"] = "APPROVED"

    print(f"\nLoan {loan_id} approved successfully!")
    print("The loan must still be disbursed before repayments can begin.")


def reject_loan():
    print("\n========== REJECT LOAN ==========")

    loan_id = get_non_empty_input("Enter loan ID: ").upper()

    loan = find_loan(loan_id)

    if loan is None:
        print("Loan not found.")
        return

    if loan["status"] != "PENDING":
        print("Only pending applications can be rejected.")
        return

    reason = get_non_empty_input("Enter rejection reason: ")

    loan["status"] = "REJECTED"
    loan["rejection_reason"] = reason

    print(f"\nLoan {loan_id} rejected successfully.")


# ============================================================
# 5. LOAN DISBURSEMENT
# ============================================================

def disburse_loan():
    print("\n========== DISBURSE LOAN ==========")

    loan_id = get_non_empty_input("Enter loan ID: ").upper()

    loan = find_loan(loan_id)

    if loan is None:
        print("Loan not found.")
        return

    if loan["status"] != "APPROVED":
        print("Only approved loans can be disbursed.")
        return

    loan["status"] = "ACTIVE"
    loan["balance"] = loan["total_payable"]
    loan["disbursement_date"] = date.today().isoformat()

    print("\nLoan successfully disbursed!")
    print(f"Loan ID: {loan['id']}")
    print(f"Amount disbursed: {format_money(loan['amount'])}")
    print(f"Total repayment: {format_money(loan['total_payable'])}")
    print(f"Outstanding balance: {format_money(loan['balance'])}")


# ============================================================
# 6. REPAYMENT MANAGEMENT
# ============================================================

def record_repayment():
    print("\n========== RECORD REPAYMENT ==========")

    loan_id = get_non_empty_input("Enter loan ID: ").upper()

    loan = find_loan(loan_id)

    if loan is None:
        print("Loan not found.")
        return

    if loan["status"] != "ACTIVE":
        print("Repayments can only be made on active loans.")
        return

    print(f"\nLoan balance: {format_money(loan['balance'])}")

    amount = get_positive_integer("Enter repayment amount (MWK): ")

    if amount > loan["balance"]:
        print("Error: Repayment exceeds the outstanding balance.")
        return

    repayment = {
        "id": generate_id("REP", repayments),
        "loan_id": loan_id,
        "amount": amount,
        "date": date.today().isoformat()
    }

    repayments.append(repayment)

    loan["amount_paid"] += amount
    loan["balance"] -= amount

    if loan["balance"] == 0:
        loan["status"] = "PAID"

        print("\nCongratulations! This loan has been fully repaid.")

    print("\nRepayment recorded successfully!")
    print(f"Repayment ID: {repayment['id']}")
    print(f"Amount paid: {format_money(amount)}")
    print(f"Total paid: {format_money(loan['amount_paid'])}")
    print(f"Remaining balance: {format_money(loan['balance'])}")
    print(f"Loan status: {loan['status']}")


def get_repayment_history():
    print("\n========== REPAYMENT HISTORY ==========")

    loan_id = get_non_empty_input("Enter loan ID: ").upper()

    loan = find_loan(loan_id)

    if loan is None:
        print("Loan not found.")
        return

    history = [
        repayment for repayment in repayments
        if repayment["loan_id"] == loan_id
    ]

    if not history:
        print("No repayments recorded for this loan.")
        return

    total = 0

    for repayment in history:
        print("-" * 35)
        print(f"Repayment ID: {repayment['id']}")
        print(f"Amount: {format_money(repayment['amount'])}")
        print(f"Date: {repayment['date']}")

        total += repayment["amount"]

    print("-" * 35)
    print(f"Total repayments: {format_money(total)}")


# ============================================================
# 7. FINANCIAL REPORTS AND ANALYTICS
# ============================================================

def get_outstanding_loans():
    """Yield loans that still have an outstanding balance."""
    for loan in loans:
        if loan["status"] == "ACTIVE" and loan["balance"] > 0:
            yield loan


def generate_financial_report():
    print("\n========== FINANCIAL REPORT ==========")

    total_borrowers = len(borrowers)
    total_applications = len(loans)

    approved = sum(1 for loan in loans if loan["status"] == "APPROVED")
    rejected = sum(1 for loan in loans if loan["status"] == "REJECTED")
    pending = sum(1 for loan in loans if loan["status"] == "PENDING")
    active = sum(1 for loan in loans if loan["status"] == "ACTIVE")
    paid = sum(1 for loan in loans if loan["status"] == "PAID")

    total_disbursed = sum(
        loan["amount"]
        for loan in loans
        if loan["status"] in ("ACTIVE", "PAID")
    )

    total_repayments = sum(
        repayment["amount"]
        for repayment in repayments
    )

    outstanding_loans = list(get_outstanding_loans())

    total_outstanding = sum(
        loan["balance"]
        for loan in outstanding_loans
    )

    # Aggregate outstanding balances by borrower.
    borrower_balances = {}

    for loan in outstanding_loans:
        borrower_id = loan["borrower_id"]

        borrower_balances[borrower_id] = (
            borrower_balances.get(borrower_id, 0) + loan["balance"]
        )

    top_borrowers = sorted(
        borrower_balances.items(),
        key=lambda item: item[1],
        reverse=True
    )[:5]

    print(f"Total borrowers: {total_borrowers}")
    print(f"Total applications: {total_applications}")
    print(f"Pending applications: {pending}")
    print(f"Approved but not disbursed: {approved}")
    print(f"Active loans: {active}")
    print(f"Rejected applications: {rejected}")
    print(f"Fully paid loans: {paid}")

    print("\n---------- FINANCIAL SUMMARY ----------")

    print(f"Total amount disbursed: {format_money(total_disbursed)}")
    print(f"Total repayments received: {format_money(total_repayments)}")
    print(f"Total outstanding balance: {format_money(total_outstanding)}")

    print("\n---------- TOP BORROWERS ----------")

    if not top_borrowers:
        print("No borrowers have outstanding loans.")
    else:
        for position, (borrower_id, balance) in enumerate(top_borrowers, start=1):
            borrower = find_borrower(borrower_id)

            print(
                f"{position}. {borrower['name']} "
                f"({borrower_id}) - {format_money(balance)}"
            )


def list_outstanding_loans():
    print("\n========== OUTSTANDING LOANS ==========")

    outstanding = list(get_outstanding_loans())

    if not outstanding:
        print("No outstanding loans.")
        return

    for loan in outstanding:
        borrower = find_borrower(loan["borrower_id"])

        print("-" * 40)
        print(f"Loan ID: {loan['id']}")
        print(f"Borrower: {borrower['name']}")
        print(f"Principal: {format_money(loan['amount'])}")
        print(f"Amount paid: {format_money(loan['amount_paid'])}")
        print(f"Outstanding: {format_money(loan['balance'])}")


# ============================================================
# 8. MAIN MENU
# ============================================================

def display_menu():
    print("\n")
    print("=" * 55)
    print("       INTELLIGENT LOAN MANAGEMENT SYSTEM")
    print("=" * 55)

    print("\nBORROWER MANAGEMENT")
    print("1. Register borrower")
    print("2. List borrowers")
    print("3. Search borrower")

    print("\nLOAN MANAGEMENT")
    print("4. Apply for loan")
    print("5. List all loans")
    print("6. View pending applications")
    print("7. Approve loan")
    print("8. Reject loan")
    print("9. Disburse loan")

    print("\nREPAYMENT MANAGEMENT")
    print("10. Record repayment")
    print("11. View repayment history")

    print("\nREPORTS AND ANALYTICS")
    print("12. Generate financial report")
    print("13. View outstanding loans")

    print("\n0. Exit")

    print("=" * 55)


def main():
    while True:
        display_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":
            register_borrower()

        elif choice == "2":
            list_borrowers()

        elif choice == "3":
            search_borrower()

        elif choice == "4":
            apply_for_loan()

        elif choice == "5":
            list_loans()

        elif choice == "6":
            list_pending_loans()

        elif choice == "7":
            approve_loan()

        elif choice == "8":
            reject_loan()

        elif choice == "9":
            disburse_loan()

        elif choice == "10":
            record_repayment()

        elif choice == "11":
            get_repayment_history()

        elif choice == "12":
            generate_financial_report()

        elif choice == "13":
            list_outstanding_loans()

        elif choice == "0":
            print("\nThank you for using the Loan Management System.")
            break

        else:
            print("\nInvalid option. Please choose a valid menu item.")


# ============================================================
# APPLICATION ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
