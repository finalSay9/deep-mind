inventory = ["Laptop", "Mouse", "OUT OF STOCK", "Keyboard", "Monitor"]

for i in inventory:
    # 1. Check for the error first
    if i == "OUT OF STOCK":
        print("Error: Missing items. Halting shipment!")
        break
    
    # 2. If it's safe, proceed with shipping
    print(f"Shipping {i}...")
