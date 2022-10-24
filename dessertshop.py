from dessert import *

def main_menu():
    print(f"Add an item from the list to the order or press 'Enter' to complete order: \n 1. Candy\n 2. Cookies\n 3. Ice Cream\n 4. Sundae\n")
    menu_input = int(input())

    if menu_input == 1:
        user_prompt_candy()
    elif menu_input == 2:
        user_prompt_cookies()
    elif menu_input == 3:
        user_prompt_icecream()
    elif menu_input == 4:
        user_prompt_sundae()
    elif menu_input == "":
        pass
        # order function where it prints out the order
    else:
        print("You must select an option from the menu")

def user_prompt_candy():
    candy_name = input("Candy Name:")
    candy_weight = input("Weight (in lbs):")
    candy_price = input("Price Per Pound:")

    def verify_candy(candy_name, candy_weight, candy_price):
        candy_name = str(candy_name)
        candy_weight = int(candy_weight)
        candy_price = float(candy_price)

        try:
            if len(candy_name) > 0:
                pass
        except ValueError:
            print("You must enter a name for the candy.")
        try:
            if candy_weight > 0:
                pass
        except ValueError:
                print("Invalid input, Candy Weight must be an number greater than 0.")
        try:
            if candy_price > 0.00:
                pass
        except ValueError:
                print("Candy price must be greater than 0.00.")
    
    verify_candy(candy_name, candy_weight, candy_price)
    return(Candy(candy_name, candy_weight, candy_price))
            
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
    return(Cookie(cookie_name, cookie_quantity, cookie_price))


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
    return(IceCream(icecream_name, icecream_scoops, icecream_price))



def user_prompt_sundae():
    icecream_name = input("Ice Cream Name:")
    icecream_scoops = input("Number Of Scoops:")
    icecream_price = input("Price Per Scoop:")
    topping_name = input("Topping Name:")
    topping_price = input("Topping Price:")

    def verify_sundae(icecream_name, icecream_scoops, icecream_price, topping_name, topping_price):
        icecream_name = str(icecream_name)
        icecream_scoops = int(icecream_scoops)
        icecream_price = int(icecream_price)
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
            if topping_name > 0:
                pass
        except ValueError:
            print("Must enter a name for the topping.")
        try:
            if topping_price > 0.00:
                pass
        except ValueError:
            print("Topping price must be greater than 0.00.")

    verify_sundae(icecream_name, icecream_scoops, icecream_price, topping_name, topping_price)
    return(Sundae(icecream_name, icecream_scoops, icecream_scoops, topping_name, topping_price))

main_menu()

