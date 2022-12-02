# from abc import *
# from enum import Enum

# class Payment(Enum):
#     methods = ['CASH', 'CARD', 'PHONE']
#     pay_message = "Pick a payment option:\n"
#     for index, item in enumerate(methods):
#         pay_message += f'{index+1} {item}\n'

#     pay_type = input('Choose an payment method: ')

#     # pay_message += 'Your choice: '

#     while pay_type.upper() not in methods:
#         pay_method = pay_type(pay_message)
    
#     print(pay_method)

class Payment():
    def pay_select():
        methods = ['CASH', 'CARD', 'PHONE']
        user_input = ''
        input_message = "Pick an option:\n"

        for index, item in enumerate(methods):
            input_message += f'{index+1}) {item}\n'

        # input_message += 'Your choice: '

        while user_input not in map(str, range(1, len(methods) + 1)):
            user_input = input(input_message)

        pay_method = methods[int(user_input) - 1]
        return(pay_method)
        # print('You picked: ' + methods[int(user_input) - 1])

# from enum import Enum
# class Payments(Enum):
#     CASH = 1
#     CARD = 2
#     PHONE = 3

# user_input = ''

# input_message = "Pick an option:\n"
# i = 0
# for method in (Payments):
#     # need to trim 'payments.' off of values
#     i += 1
#     input_message += f'{i}) {str(method).strip("Payments.")}\n'

# print(input_message)
