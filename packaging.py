from abc import *

# To Do
    # Two methods that define abstract method 'packaging'
        # Use property decorator
        # Make setter an abstract method
    # Implement __subclasshook__ magic method
        # Test if a class is a subclass of packaging

# abstract base class
class packaging(ABC):

    @property
    def get_packaging(self):
        return self.packaging

    # @packaging.setter
    def set_packaging(self, value):
        print(self.packaging)

    packaging = property(get_packaging, set_packaging)

    @classmethod
    def ___subclasshook__(cls):
    # test whether a class is a subclass of packaging
        if cls is packaging:
            if any("__packaging__" in DessertItem):
                return True
        return NotImplemented
