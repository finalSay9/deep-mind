# Here is your machine's inventory and prices
vending_items = ["Soda", "Chips", "Candy", "Water"]
vending_prices = [2.50, 1.50, 1.00, 1.20]

for index, item in enumerate(vending_items, start=1):
    print(f"{index} {item}")