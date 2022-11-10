import pytest
import dessert

DessertItem = dessert.DessertItem 
Candy = dessert.Candy
Cookie = dessert.Cookie
IceCream = dessert.IceCream
Sundae = dessert.Sundae

def newCandy():
  return Candy("new Candy", 2.00, 1.00)

def newCookie():
  return Cookie("test Cookie", 3, 5.00)

def newIceCream():
  return IceCream("test Ice Cream", 3, 1.00)

def newSundae():
  return Sundae("test", 2, 1.50, "test Sundae Topping", 2.00)

def test_tax():
  assert newCandy().tax_percent == 7.25
  assert newCookie().tax_percent == 7.25
  assert newIceCream().tax_percent == 7.25
  assert newSundae().tax_percent == 7.25

def test_Candy():
  # assert newCandy().name == "new Candy"
  assert newCandy().candy_weight == 2.00
  assert newCandy().price_per_pound == 1.00

def test_Cookie():
  # assert newCookie.name == "test Cookie"
  assert newCookie().cookie_quantity == 3
  assert newCookie().price_per_dozen == 5.00

def test_IceCream():
  # assert newIceCream.name = "test Ice Cream"
  assert newIceCream().scoop_count == 3
  assert newIceCream().price_per_scoop == 1.00

def test_Sundae():
  assert newSundae().scoop_count == 2
  assert newSundae().price_per_scoop == 1.50
  assert newSundae().topping_name == "test Sundae Topping"
  assert newSundae().topping_price == 2.00

def test_cost():
  assert newCandy().calculate_cost() == 2.00
  assert newCookie().calculate_cost() == 5.00 * (3/12)
  assert newIceCream().calculate_cost() == 3.00
  assert newSundae().calculate_cost() == 5.00

def test_tax():
  assert newCandy().calculate_tax() == 0.14
  assert newCookie().calculate_tax() == 0.09
  assert newIceCream().calculate_tax() == 0.22
  assert newSundae().calculate_tax() == 0.36

def test_packaging():
  assert newCandy().packaging == "Bag"
  assert newCookie().packaging == "Box"
  assert newIceCream().packaging == "Bowl"
  assert newSundae().packaging == "Boat"