import pytest
from dessertshop import Customer

def newCustomer():
#   return Customer('Test Name', 3, [['Test Order 1'], ['Test order 3']])
    return Customer('Test Name')

def test_customers():
  assert newCustomer().customer_name == 'Test Name'
  assert newCustomer().customer_id == 3
  assert newCustomer().order_history[0] == ['Test Order 1']
  assert newCustomer().order_history[1] == ['Test Order 2']

