# Here is your machine's inventory and prices
vending_items = ["Soda", "Chips", "Candy", "Water"]
vending_prices = [2.50, 1.50, 1.00, 1.20]
inventrory_stock = []

while True:
   
    
    for i, item in enumerate(vending_items, start=1):
        price = vending_prices[i-1]
        print(f"{i}. {item} (${price:.2f})")

    

    choice = int(input("enter your choice(1-4): "))
    if choice < 0 or choice > len(vending_items):
        print("\nenter a valid choice: ")
    else:
        i = choice - 1
        item = vending_items[i]
        price = vending_prices[i]
        print(f"{item} {price}")