class Vending:
    vending_items = ["Soda", "Chips", "Candy", "Water"]
    vending_prices = [2.50, 1.50, 1.00, 1.20]
    inventory_stock = []

    def __init__(self):
        # Vending.inventory_stock.append()
        pass

    def display_items(self):
        for i, item in enumerate(self.vending_items, start=1):
            self.price = self.vending_prices[i-1]
            print(f"{i}. {item} {self.price}")

    @staticmethod
    def choices():
        choice = int(input('enter your choice: '))
        index = choice -1
        item = Vending.vending_items[index]
        price = Vending.vending_prices[index]
        if choice < 0 or choice > len(Vending.vending_items):
            print("enter valid choice")
        else:
            Vending.vending_items.remove()
            print(f"{item} {price}")

    def count(self):
        return len(Vending.vending_items)
    
    @classmethod
    def inventory(cls):
        pass
        

customer = Vending()
customer.display_items()
customer.choices()
customer.count()