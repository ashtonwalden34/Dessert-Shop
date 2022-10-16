class DessertItem():
    def __init__(self, name=""):
        self.name = name

class Candy(DessertItem):
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        print(f'{self.candy_weight}lbs at ${self.price_per_pound} per pound.')

class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity = 0, price_per_dozen = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        print(f"{self.cookie_quantity} cookies at ${self.price_per_dozen} per dozen.")

class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        print(f"{self.scoop_count}s at ${self.price_per_scoop} per scoop.")

class Sundae(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name = "", topping_price = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.topping_name = topping_name
        self.topping_price = topping_price
        print(f"{self.topping_name} costs ${self.topping_price}.")

class Order():
    def __init__(self, order = []):
        self.order = order
    def add_dessert(self, dessert_item):
        assert isinstance(dessert_item, DessertItem)
        self.order.append(dessert_item)

def main():
    Order.add_dessert(Candy("Candy Corn", 1.5, .25))
    Order.add_dessert(Candy("Gummy Bears", .25, .35))
    Order.add_dessert(Cookie("Chocolate Chip", 6, 3.99))
    Order.add_dessert(IceCream("Pistachio", 2, .79))
    Order.add_dessert(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    Order.add_dessert(Cookie("Oatmeal Raisin", 2, 3.45))