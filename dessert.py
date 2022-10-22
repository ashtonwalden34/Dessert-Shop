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
        # tax = item_cost * tax_percent
        pass

class Candy(DessertItem):
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0.00):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        # print(f'{self.candy_weight}lbs at ${self.price_per_pound} per pound.')
    #overriding abstract methods?
    def calculate_cost(self):
        # super().calculate_cost()
        cost = self.candy_weight * self.price_per_pound
        # print(f'Cost: ${cost}')
        return(round(cost, 2))
    def calculate_tax(self):
        # super().calculate_tax()
        tax = self.calculate_cost() * (self.tax_percent / 100)
        # print(f'Tax: ${tax}')
        return(round(tax, 2))

class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity = 0, price_per_dozen = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        # print(f"{self.cookie_quantity} cookies at ${self.price_per_dozen} per dozen.")
     #overriding abstract methods
    def calculate_cost(self):
        # super().calculate_cost()
        cost = self.cookie_quantity * (self.price_per_dozen / 12)
        # print(f'{self.cookie_quantity} {self.name} cookies will cost: {item_cost}')
        # print(f'This is the cost of cookies: {cost}')
        return(round(cost, 2))
    def calculate_tax(self):
        # super().calculate_tax()
        tax = self.calculate_cost() * (self.tax_percent / 100)
        # print(f'Tax: ${tax}')
        return(round(tax, 2))

class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        # print(f"{self.scoop_count}s at ${self.price_per_scoop} per scoop.")

    def calculate_cost(self):
        # super().calculate_cost()
        cost = self.scoop_count * self.price_per_scoop
        # print(f'{self.scoop_count} scoops of {self.name} will cost: {cost}')
        return(round(cost, 2))

    def calculate_tax(self):
        # super().calculate_tax()
        tax = self.calculate_cost() * (self.tax_percent / 100)
        # print(f'Tax: ${tax}')
        return(round(tax, 2))

class Sundae(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name = "", topping_price = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.topping_name = topping_name
        self.topping_price = topping_price
        # print(f"{self.topping_name} costs ${self.topping_price}.")

    def calculate_cost(self):
        # super().calculate_cost()
        cost = (self.scoop_count * self.price_per_scoop) + self.topping_price
        # print(f'{self.scoop_count} scoops of {self.name} will cost: {cost}')
        return(round(cost, 2))

    def calculate_tax(self):
        # super().calculate_tax()
        tax = self.calculate_cost() * (self.tax_percent / 100)
        # print(f'Tax: ${tax}')
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
            # print(f'"test cost index loop thingy" ${subtotal}')
        # print("%.2f" % subtotal)
        return round(subtotal, 2)
    def order_tax(self):
        taxes = 0.00
        for index in range(len(self.order)):
            taxes += self.order[index].calculate_tax()
            # print(f'"test cost index loop thingy" ${subtotal}')
        # print("%.2f" % taxes)
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
    order.add_dessert(Candy("Candy Corn", 1.5, .25))
    order.add_dessert(Candy("Gummy Bears", .25, .35))
    order.add_dessert(Cookie("Chocolate Chip", 6, 3.99))
    order.add_dessert(IceCream("Pistachio", 2, .79))
    order.add_dessert(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order.add_dessert(Cookie("Oatmeal Raisin", 2, 3.45))

    print("Receipt \n---------------")

    for dessert_item in order.get_dessert():
        # print(f'{dessert_item.name} Cost: ${dessert_item.calculate_cost().item_cost} Tax: ${dessert_item.item_tax}')
        # print(dessert_item.name + "%.2f" % dessert_item.calculate_cost() + f"{'': ^5}" + "%.2f" % dessert_item.calculate_tax())
        print(f"{dessert_item.name :18} $ {dessert_item.calculate_cost() : <7}Tax: $ {dessert_item.calculate_tax() : <5}")

    print ("--------------- \n--------------- \n---------------")
    # print("Subtotal: $" + "%.2f" % order.order_cost())
    # print("Total Tax: $" + str("%.2f" % order.order_tax()))
    print(f"Subtotal: ${order.order_cost()} Tax: ${order.order_tax() : <5}")
    print(f'Total: ${order.order_total()}')
    print('Item Total: ' + str(order.get_length()))

if __name__ == "__main__":
    main()


# *** OUTLINE FOR USER INPUT TO BE USED LATER ***
# user_selection = input("0 - complete order  \n1 - Add an additional item to order \n")

# def input_verify(user_selection):
#     val = int(user_selection)
#     try: 
#         if val == 0 or val == 1:
#             pass
#     except ValueError:
#         print("Invalid input, must enter a '0' or a '1'.")

# input_verify(user_selection)
