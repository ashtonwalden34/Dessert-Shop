'''Dessert Shop'''

from unicodedata import name


class DessertItem():
    def __init__(self, name=""):
        self.name = name

class Candy():
    def __init__(self, candy_weight = 0.0, price_per_pound = 0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

class Cookie():
    def __init__(self, cookie_quantity = 0, price_per_dozen = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

class IceCream():
    def __init__(self, scoop_count = 0, price_per_scoop = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

class Sundae():
    def __init__(self, topping_name = "", topping_price = 0.0):
        super().__init__(name)
        self.topping_name = topping_name
        self.topping_price = topping_price

