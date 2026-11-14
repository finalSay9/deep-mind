print("=" * 52)
print("\n           MICRO FINANCE MANAGEMENT\n")
print("=" * 52)


borrowers = []
loans = []
next_id = 1  
loan_id = 1
#creating a user
def createUser():
    global next_id

    name = input("enter users's name: ")
    phone = input("enter phone number: ")
    monthly_income = input("enter montly income: ")
    address = input("enter address: ")
    user_id = f"BRW-{next_id:03d}"
    next_id += 1
    
    new_borrower =  {
        "id": user_id,
        "name": name,
        "phone": phone,
        "mothly_income": monthly_income,
        "address": address
    }
    borrowers.append(new_borrower)
    return new_borrower
    

#search borrower
def search():
    for borrower in borrowers:
        user = input("enter the name: ")
        if user == borrower['name']:
            print(borrower)


#loan application
def apply_loan():
    global loan_id
    #verify the user by phone number
    interest_rate = 18
    duration = 12
    phone = input("enter your phone number: ")
    loanId = f"LON-{loan_id:03d}"
    loan_id += 1


    for check in borrowers:
        if phone != check['phone']:
            print("sorry you can't apply, you're not a registered user")
        else:
            amount = int(input("enter amount: (max 500000)"))
            new_loan = {
                "id": loanId,
                "user_id": check['id'],
                "phone": phone,
                "amount": amount,
                "interest": interest_rate * amount,
                "duration": duration,
                "status":  "PENDING"
            }
            loans.append(new_loan)
            return new_loan

def approve_loan():
    #check if loan is available by id
    for loan in loans:
        id = input("enter loan id: ")
        if id == loan['id'] and loan['status'] == "PENDING":
            loan['status'] = "APPROVED"
        print(loan) 

def reject_loan():
    #check if loan is available by id
    for loan in loans:
        id = input("enter loan id: ")
        if id == loan['id'] and loan['status'] == "PENDING":
            loan['status'] = "REJECTED"
        print(loan) 


def process_repayment():
    for loan in loans:
        #id to check loan balance
        id = input("enter the id to check the balance: ")
        if id == loan['id']:
            print(f"your loan balance is {loan['amount']}")
        amount = int(input("enter amount repay: "))
        process = loan['amount'] - amount
        print(f"you have successfully repaid your loan, your balace is {process}")

def finacial_report():
    total_borrowers = len(borrowers)
    total_loans = len(loans)
    total_money = 0
    all_approved = 0
    all_pending = 0
    all_rejected = 0
    #calculate total number of applicants
    for loan in loans:
        if loan["status"] == "APPROVED":
            all_approved += 1
            total_money += loan["amount"]
        elif loan["status"] == "PENDING":
            all_pending += 1
        elif loan["status"] == "REJECTED":
            all_rejected += 1

    print("\n" + "=" * 35)
    print("         FINANCIAL REPORT")
    print("=" * 35)
    print(f"Registered Borrowers : {total_borrowers}")
    print(f"Total Loan Requests  : {total_loans}")
    print(f"Approved Loans       : {all_approved}")
    print(f"Pending Loans        : {all_pending}")
    print(f"Rejected Loans       : {all_rejected}")
    print(f"Total Disbursed      : {total_money}")
    print("=" * 35)
        


while True:
    print(
        "\n1. Register Borrower"
        "\n2. View Borrowers"
        "\n3. Search Borrower"
        "\n4. Apply for Loan"
        "\n5. Approve Loan"
        "\n6. Reject Loan"
        "\n7. Process Repayment"
        "\n8. View Loan Details"
        "\n9. Financial Report"
        "\n10. Exit"
    )
    option = int(input("\nchoose your option: "))
    if option == 1:
        print(createUser())

    if option == 2:
        print(borrowers)

    if option == 3:
        search()

    if option == 4:
        print(apply_loan())
    
    if option == 5:
        approve_loan()

    if option == 7:
        process_repayment()
    
    if option == 8:
        print(loans)
    
    if option == 9:
        finacial_report()
    
    if option == 10:
        print("Thank you choosing us!!")
        break