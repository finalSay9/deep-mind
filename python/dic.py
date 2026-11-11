transactions = [
    {"id": 1, "amount": 500, "status": "SUCCESS"},
    {"id": 2, "amount": 200, "status": "FAILED"},
    {"id": 3, "amount": 800, "status": "SUCCESS"},
    {"id": 4, "amount": 100, "status": "SUCCESS"},
    {"id": 5, "amount": 300, "status": "FAILED"}
]

total_success_count = 0
total_failed_count = 0
total_success_amount = 0
highest_success_amount = 0

for transaction in transactions:
    # Handle Failed Transactions
    if transaction['status'] == "FAILED":
        total_failed_count += 1
        
    # Handle Successful Transactions
    elif transaction['status'] == "SUCCESS":
        total_success_count += 1
        total_success_amount += transaction['amount']
        
        # Track the highest successful amount
        if transaction['amount'] > highest_success_amount:
            highest_success_amount = transaction['amount']

print(f"Failed transaction count: {total_failed_count}")
print(f"Successful transaction count: {total_success_count}")
print(f"Total amount for successful transactions: {total_success_amount}")
print(f"Highest successful transaction amount: {highest_success_amount}")
