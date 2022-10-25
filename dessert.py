from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name="", tax_percent = 7.25):
        self.name = name
        self.order = []
        self.tax_percent = tax_percent

    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def calculate_tax(self):
        pass


class Candy(DessertItem):
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0.00):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    #overriding abstract methods?
    def calculate_cost(self):
        cost = self.candy_weight * self.price_per_pound
        return(round(cost, 2))
    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return(round(tax, 2))
    def add_to_order(self):
        Order().add_dessert(Candy(self.name, self.candy_weight, self.price_per_pound))

class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity = 0, price_per_dozen = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
     #overriding abstract methods
    def calculate_cost(self):
        cost = self.cookie_quantity * (self.price_per_dozen / 12)
        return(round(cost, 2))
    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return(round(tax, 2))

class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop
        return(round(cost, 2))

    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return(round(tax, 2))

class Sundae(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name = "", topping_price = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        cost = (self.scoop_count * self.price_per_scoop) + self.topping_price
        return(round(cost, 2))

    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return(round(tax, 2))

class Order():
    def __init__(self, order = []):
        self.order = order
    def add_dessert(self, dessert_item):
        assert isinstance(dessert_item, DessertItem)
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

def main():
    order = Order()

    print("Receipt \n---------------")
    for dessert_item in order.get_dessert():
        print(f"{dessert_item.name :18} $ {dessert_item.calculate_cost() : <7}Tax: $ {dessert_item.calculate_tax() : <5}")
    print ("--------------- \n--------------- \n---------------")
    print(f"Subtotal: ${order.order_cost()} Tax: ${order.order_tax() : <5}")
    print(f'Total: ${order.order_total()}')
    print('Item Total: ' + str(order.get_length()))

if __name__ == "__main__":
    main()

