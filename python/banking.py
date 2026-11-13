transactions = [
    {"id": 1, "user": "Evan", "amount": 5000, "type": "DEPOSIT"},
    {"id": 2, "user": "John", "amount": 2000, "type": "WITHDRAWAL"},
    {"id": 3, "user": "Evan", "amount": 1500, "type": "WITHDRAWAL"},
    {"id": 4, "user": "Mary", "amount": 7000, "type": "DEPOSIT"},
    {"id": 5, "user": "John", "amount": 3000, "type": "DEPOSIT"},
    {"id": 6, "user": "Mary", "amount": 1000, "type": "WITHDRAWAL"},
]


successful_deposites = []

for transaction in transactions:
    successful_deposites.append(transaction)
print(successful_deposites)