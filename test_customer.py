import pytest
from dessertshop import Customer

def newCustomer():
#   return Customer('Test Name', 3, [['Test Order 1'], ['Test order 3']])
    # return Customer('Test Name')
  return Customer('Test 1', 0)

def otherCustomer():
  return Customer('Test 2', 0)

# def test_customers():
#   assert newCustomer().customer_name == 'Test Name'
#   assert newCustomer().customer_id == 3
#   assert newCustomer().order_history[0] == ['Test Order 1']
#   assert newCustomer().order_history[1] == ['Test Order 2']

def test_customer_id():
  assert newCustomer().customer_id != otherCustomer().customer_id