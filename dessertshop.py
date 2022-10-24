def main_menu():
    print(f"Add another item from the list to the order or press 'Enter' to complete order:" + 
    "\n 1. Candy\n 2. Cookies\n 3. Ice Cream\n 4. Sundae")

def user_prompt_candy():
    candy_name = input("Candy Name:")
    candy_weight = input("Weight (in lbs):")
    candy_price = input("Price Per Pound:")

def user_prompt_cookies():
    cookie_name = input("Cookie Name:")
    cookie_quantity = input("Quantity:")
    cookie_price = input("Price Per Dozen:")

def user_prompt_icecream():
    icecream_name = input("Ice Cream Name:")
    icecream_scoops = input("Number Of Scoops:")
    icecream_price = input("Price Per Scoop:")

def user_prompt_sundae():
    icecream_name = input("Ice Cream Name:")
    icecream_scoops = input("Number Of Scoops:")
    icecream_price = input("Price Per Scoop:")
    topping_name = input("Topping Name:")
    topping_price = input("Topping Price:")

main_menu()

def verify_input():
    pass


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