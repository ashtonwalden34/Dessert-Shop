'''Dessert Shop'''

from unicodedata import name


class DessertItem():
    def __init__(self, name=""):
        self.name = name

class Candy():
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def print_candy(self):
        print(f"{self.candy_weight}lbs at ${self.price_per_pound} per pound.")

class Cookie():
    def __init__(self, name, cookie_quantity = 0, price_per_dozen = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def print_cookie(self):
        print(f"{self.cookie_quantity} cookies at ${self.price_per_dozen} per dozen.")

class IceCream():
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def print_ice_cream(self):
        print(f"{self.scoop_count}s at ${self.price_per_scoop} per scoop.")

class Sundae():
    def __init__(self, topping_name = "", topping_price = 0.0):
        super().__init__(name)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def print_topping(self):
        print(f"{self.topping_name} costs ${self.topping_price}.")

        		
        # print(f"{helen.first_name}{helen.last_name}is a member of the {helen.union}.") 