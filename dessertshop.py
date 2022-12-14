from dessert import *
from payment import *
from abc import *

class Customer():
    # def __init__(self, customer_name):
    #     self.customer_name = customer_name
    #     self.order_history = []
    #     self.customer_id = int
    def __init__(self, customer_name, customer_id):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.order_history = []
        self.total_orders = 0

    def add2history(customer_name, Customer):
        customer_db.append()
        return(Customer)

# customer_db: Dict[str, Customer]
customer_db = {}

def customer_menu():
    global customer_db
    # total_orders = len(Customer.order_history)
    print('Please enter your name:')
    name = str(input()).upper()
    customer_id = len(customer_db)
    # Customer.__setattr__(Customer, 'customer_id', customer_id)
    print(f'Customer Name: {name}     Customer ID: {Customer(name, customer_id).customer_id}       Total Orders: ')

    if name in customer_db:
        # add order
        # Customer.total_orders += 1
        # print(Customer.total_orders)
        pass
    else:
        customer_db[name] = (Customer(name, customer_id))	
    # print(customer_db)
    print('Would you like to start another order?')
    new_order_input = str(input()).upper()
    print('\n')

    # print(Customer.order_history[0])
    if new_order_input == 'Y':
        main_menu()
    else:
        pass

def main_menu():
    print(f"Add an item from the list to the order or press 0 to complete order: \n 1. Candy\n 2. Cookies\n 3. Ice Cream\n 4. Sundae\n")
    menu_input = int(input())
    self = Payment

    if menu_input == 1:
        user_prompt_candy()
    elif menu_input == 2:
        user_prompt_cookies()
    elif menu_input == 3:
        user_prompt_icecream()
    elif menu_input == 4:
        user_prompt_sundae()
    elif menu_input == 0:
        # print(f"Enter a payment method:")
        # pay_method = Order.pay_method(self)
        main()
        customer_menu()
        # order function where it prints out the order
    else:
        print("You must select an option from the menu")

def user_prompt_candy():
    candy_name = str(input("Candy Name:"))
    candy_weight = float(input("Weight (in lbs):"))
    candy_price = float(input("Price Per Pound:"))

    def verify_candy(candy_name, candy_weight, candy_price):
        candy_name = str(candy_name)
        candy_weight = float(candy_weight)
        candy_price = float(candy_price)
        try:
            if len(candy_name) > 0:
                pass
        except ValueError:
            print("You must enter a name for the candy.")
        try:
            if candy_weight > 0.00:
                pass
        except ValueError:
                print("Invalid input, Candy Weight must be an number greater than 0.")
        try:
            if candy_price > 0.00:
                pass
        except ValueError:
                print("Candy price must be greater than 0.00.")
    
    verify_candy(candy_name, candy_weight, candy_price)
    candy_obj = Candy(candy_name, candy_weight, candy_price)
    order = Order()
    order.add_dessert(candy_obj)
    main_menu()
            
def user_prompt_cookies():
    cookie_name = input("Cookie Name:")
    cookie_quantity = input("Quantity:")
    cookie_price = input("Price Per Dozen:")

    def verify_cookies(cookie_name, cookie_quantity, cookie_price):
        cookie_name = str(cookie_name)
        cookie_quantity = int(cookie_quantity)
        cookie_price = float(cookie_price)

        try:
            if len(cookie_name) > 0:
                pass
        except ValueError:
            print("You must enter a name for the cookie.")
        try:
            if cookie_quantity > 0:
                pass
        except ValueError:
            print("You must enter a quantity greater than 0 for the cookies.")
        try:
            if cookie_price > 0.00:
                pass
        except ValueError:
            print("Cookie price must greater than 0.00")

    verify_cookies(cookie_name, cookie_quantity, cookie_price)
    cookie_obj = Cookie(cookie_name, cookie_quantity, cookie_price)
    order = Order()
    order.add_dessert(cookie_obj)
    main_menu()


def user_prompt_icecream():
    icecream_name = input("Ice Cream Name:")
    icecream_scoops = input("Number Of Scoops:")
    icecream_price = input("Price Per Scoop:")

    def verify_icecream(icecream_name, icecream_scoops, icecream_price):
        icecream_name = str(icecream_name)
        icecream_scoops = int(icecream_scoops)
        icecream_price = float(icecream_price)

        try:
            if len(icecream_name) > 0:
                pass
        except ValueError:
            print("Must enter a name for the ice cream.")
        try:
            if icecream_scoops > 0:
                pass
        except ValueError:
            print("Ice Cream scoops must be greater than 0")
        try:
            if icecream_price > 0.00:
                pass
        except ValueError:
            print("Ice Cream price must be greater than 0.00.")
    
    verify_icecream(icecream_name, icecream_scoops, icecream_price)
    icecream_obj = IceCream(icecream_name, icecream_scoops, icecream_price)
    order = Order()
    order.add_dessert(icecream_obj)
    main_menu()
    

def user_prompt_sundae():
    icecream_name = input("Ice Cream Name:")
    icecream_scoops = input("Number Of Scoops:")
    icecream_price = input("Price Per Scoop:")
    topping_name = input("Topping Name:")
    topping_price = input("Topping Price:")

    def verify_sundae(icecream_name, icecream_scoops, icecream_price, topping_name, topping_price):
        icecream_name = str(icecream_name)
        icecream_scoops = int(icecream_scoops)
        icecream_price = float(icecream_price)
        topping_name = str(topping_name)
        topping_price = float(topping_price)

        try:
            if len(icecream_name) > 0:
                pass
        except ValueError:
            print("Must enter a name for the ice cream.")
        try:
            if icecream_scoops > 0:
                pass
        except ValueError:
            print("Ice Cream scoops must be greater than 0")
        try:
            if icecream_price > 0.00:
                pass
        except ValueError:
            print("Ice Cream price must be greater than 0.00.")
        try:
            if len(topping_name) > 0:
                pass
        except ValueError:
            print("Must enter a name for the topping.")
        try:
            if topping_price > 0.00:
                pass
        except ValueError:
            print("Topping price must be greater than 0.00.")

    verify_sundae(icecream_name, icecream_scoops, icecream_price, topping_name, topping_price)
    sundae_obj = Sundae(icecream_name, icecream_scoops, icecream_price, topping_name, topping_price)
    order = Order()
    order.add_dessert(sundae_obj)
    main_menu()

main_menu()
