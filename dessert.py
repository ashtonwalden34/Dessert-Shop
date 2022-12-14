from abc import ABC, abstractmethod
from packaging import *
from payment import Payment
from functools import total_ordering
from typing import *


T = TypeVar('T')
class SameItem(ABC):
    def is_same_as(self, other:T) -> bool:
        if isinstance(other, self):
            return(True)
        else:
            return(False)

@total_ordering
class DessertItem(ABC):
    def __init__(self, name="", tax_percent = 7.25, packaging = ""):
    # def __init__(self, name="", tax_percent = 7.25, packaging = ""):
        self.name = name
        self.order = []
        self.tax_percent = tax_percent
    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def calculate_tax(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
    
    # @abstractproperty
    # def packaging(Package):
    #     # @property
    #     # getter
    #     # setter
    #     # @packaging.setter

    def _is_valid_operand(self, other):
        return (hasattr(other, "price_per_pound") or 
            hasattr(other, "price_per_dozen") or 
            hasattr(other, "price_per_scoop") or
            hasattr(other, "topping_price"))

    def __eq__(self, other):
        # if not self._is_valid_operand(other):
        #     return NotImplemented
        return ((self.calculate_cost()) == (other.calculate_cost()))

    def __lt__(self, other):
        # if not self._is_valid_operand(other):
        #     return NotImplemented
        return ((self.calculate_cost()) < (other.calculate_cost()))
 

class Candy(DessertItem):
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0.00, packaging = "Bag"):
    # def __init__(self, name, candy_weight = 0.0, price_per_pound = 0.00, packaging = "Bag"):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = packaging
    #overriding abstract methods?
    def calculate_cost(self):
        cost = self.candy_weight * self.price_per_pound
        return(round(cost, 2))
    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return(round(tax, 2))
    def add_to_order(self):
        # Order().add_dessert(Candy(self.name, self.candy_weight, self.price_per_pound))
        Order().add_dessert(f'{self.name} \n {self.candy_weight}lbs @ ${self.price_per_pound}: ${self.calculate_cost()} [Tax: ${self.calculate_tax()}]').__str__()
    def __str__(self):
        return(f'{self.name} ({self.packaging})\n {self.candy_weight} lbs @ ${self.price_per_pound} per pound: ${self.calculate_cost()}'.ljust(50, ' ') + f'[Tax: ${self.calculate_tax()}]')
        # return(f'{self.calculate_cost()}'.ljust(5, '$') + f'{self.calculate_tax()}')

    def is_same_as(self, other: "Candy"):
        if self.name == other.name and self.price_per_pound == other.price_per_pound:
            self.candy_weight = self.candy_weight + other.candy_weight
        else:
            return(False)


class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity = 0, price_per_dozen = 0.0, packaging = "Box"):
    # def __init__(self, name, cookie_quantity = 0, price_per_dozen = 0.0, packaging = "Box"):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = packaging
     #overriding abstract methods
    def calculate_cost(self):
        cost = int(self.cookie_quantity) * (float(self.price_per_dozen) / 12)
        return(round(cost, 2))
    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return(round(tax, 2))
    def __str__(self):
        return(f'{self.name} ({self.packaging})\n {self.cookie_quantity} @ ${self.price_per_dozen}/dozen: ${self.calculate_cost()}'.ljust(50, ' ') + f'[Tax: ${self.calculate_tax()}]')

    def is_same_as(self, other: "Cookie"):
        if self.name == other.name and self.price_per_dozen == other.price_per_dozen:
            self.candy_weight = self.cookie_quantity + other.cookie_quantity
        else:
            return(False)


class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0, packaging = "Bowl"):
    # def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0, packaging = "Bowl"):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = packaging
    def calculate_cost(self):
        cost = int(self.scoop_count) * float(self.price_per_scoop)
        return(round(cost, 2))
    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return(round(tax, 2))
    def __str__(self):
        return(f'{self.name} ({self.packaging}) \n {self.scoop_count} scoops @ ${self.price_per_scoop}: ${self.calculate_cost()}'.ljust(50, ' ') + f'[Tax: ${self.calculate_tax()}]')


class Sundae(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name = "", topping_price = 0.0, packaging = "Boat"):
    # def __init__(self, name, scoop_count, price_per_scoop, topping_name = "", topping_price = 0.0, packaging = "Boat"):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = packaging
    def calculate_cost(self):
        cost = (int(self.scoop_count) * float(self.price_per_scoop)) + float(self.topping_price)
        return(round(cost, 2))
    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return(round(tax, 2))
    def __str__(self):
                return(f'{self.name} with {self.topping_name} ({self.packaging})\n {self.scoop_count} scoops @ ${self.price_per_scoop} with topping @ ${self.topping_price}: ${self.calculate_cost()}'.ljust(75, ' ') + f'[Tax: ${self.calculate_tax()}]')


class Order():
    def __init__(self, order = []):
        self.order = order
    def add_dessert(self, dessert_item):
        # assert isinstance(dessert_item, DessertItem)
        self.order.append(dessert_item)
    def get_dessert(self):
        return self.get_by_type(DessertItem)
    def get_by_type(self, typ):
        return[dessert_item for dessert_item in self.order if isinstance(dessert_item, typ)]
    def order_cost(self):
        subtotal = 0.00
        for index in range(len(self.order)):
            subtotal += self.order[index].calculate_cost()
        return round(subtotal, 2)
    def order_tax(self):
        taxes = 0.00
        for index in range(len(self.order)):
            taxes += self.order[index].calculate_tax()
        return round(taxes, 2)
    def order_total(self):
       total =  self.order_tax() + self.order_cost()
       return(round(total, 2))
    def get_length(self):
        length = 0
        for index in range(len(self.order)):
            length += 1
        return(length)
    def pay_method(self):
        self.pay_method = Payment.pay_select()
        return(self.pay_method)
    
    # sort attempt
    # def sort(self):
    #     sorted_order = []
    #     i = 0
    #     for item in self.order:
    #         item.__lt__(self.order[i + 1])
    #         sorted_order.append(item)

    # # Combine Like Items
    # def combine(self, other):
    #     for item in self.order():
    #         if item.is_same_as(item, other): 
    #             Candy.is_same_as(self, other="Candy")
    #             Cookie.is_same_as(self, other="Cookie")
    #             pass
    #         else:
    #             self.order.append(DessertItem)

def main():
    order = Order()
    # sort = order.sort()
    payment_mehtod = order.pay_method()
    # print(sort)
    print("\n \n \n")
    print("Receipt \n---------------")
    # i = 0
    for dessert_item in order.get_dessert():
        # sort
        # dessert_item.__lt__(dessert_item)
        # dessert_item.__lt__(order[i + 1])
        print(dessert_item.__str__())
    print ("--------------- \n--------------- \n---------------")
    print(f"Subtotal: ${order.order_cost()} Tax: ${order.order_tax() : <5}")
    print(f'Total: ${order.order_total()}')
    print('Item Total: ' + str(order.get_length()))
    print ("---------------")
    print(f'Paid with {payment_mehtod} \n \n \n')
    # print(order)
    print ("---------------")

if __name__ == "__main__":
    main()

