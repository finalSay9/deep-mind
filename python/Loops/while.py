# Here is your machine's inventory and prices
vending_items = ["Soda", "Chips", "Candy", "Water"]
vending_prices = [2.50, 1.50, 1.00, 1.20]

for i in range(len(vending_items)):
    item = vending_items[i]
    price = vending_prices[i]
    item_number = i + 1
    print(f"• {item_number}. {item} (${price:.2f})")
    if i == 5:
        continue
    while True:
        print("use 1-4 to choose item and 0 to leave")
        print(f"• {item_number}. {item} (${price:.2f})")
        choice = int(input("\nenter your choice: "))
        if choice < 0 & choice > 4:
            print("follow instructions and enter a valid number")
        

