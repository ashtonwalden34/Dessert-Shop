from typing_extensions import Self
import pytest

from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

# content of test_sample.py

def test_ice_cream(IceCream):
    IceCream.print_ice_cream() == ""



if __name__ == '__main__':
    pytest.main()