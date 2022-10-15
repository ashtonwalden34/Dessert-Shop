class PetStore:
    name = "Pet Peddlers"
    def __init__(self,id_number):
        self.id_number = id_number
        self.animals = []
        self.featured_pet = None

    def add_pet(self,animal):
        assert isinstance(animal,Animal)
        self.animals.append(animal)

    def remove_pet(self,animal):
        ''' Removes a pet. Shows a try else clause '''
        try:
            self.animals.remove(animal)
        except:
            print("No such animal")
        else:
            print(animal,'removed')

    def feature(self,name):
        '''
            Features a selected pet.
            Illustrates the use of a loop else clause
        '''
        for pet in self.animals:
            if pet.name == name:
                self.featured_pet = pet
                print('Featured pet..',pet)
                break                
        else:
            print("No such animal")

    def get_featured(self):
        return self.featured_pet

    def feed(self):
        for pet in self.animals:
            pet.eat()

    def get_mammals(self):
        return self.get_by_type(Mammal)

    def get_birds(self):
        return self.get_by_type(Bird)

    def get_reptiles(self):
        return self.get_by_type(Reptile)

    def get_amphibians(self):
        return self.get_by_type(Amphibian)

    def get_fish(self):
        return self.get_by_type(Fish)

    def get_by_type(self,typ):
        return [pet for pet in self.animals if isinstance(pet,typ)]

from abc import ABC
class Animal(ABC):
    '''
        Abstract class for all animals.
        Holds what is common for all animals: name, eat and __str__ methods
    '''
    def __init__(self,name):
        self.name = name
    def eat(self):
        '''
            Note that self.diet below actually retrieves type(self).diet
        '''
        print(self.name,'eating',self.diet)
    def __str__(self):
        '''
            Note how we get the class name with type and __name__.
        '''
        return type(self).__name__ + ": " + self.name
class Mammal(Animal):
    pass
class Cat(Mammal):
    diet = 'mice'
class Dog(Mammal):
    diet = 'kibble'
class Reptile(Animal):
    pass
class Snake(Reptile):
    diet = 'rodents'
class Turtle(Reptile):
    diet = 'carrots'
class Bird(Animal):
    pass
class Parakeet(Bird):
    diet = 'seed'
class Toucan(Bird):
    diet = 'caterpillars'
class Amphibian(Animal):
    pass
class Frog(Amphibian):
    diet = 'flies'
class Newt(Amphibian):
    diet = 'worms'
class Fish(Animal):
    pass
class Koi(Fish):
    diet = 'algae'
class Guppy(Fish):
    diet = 'flakes'


store = PetStore(1)
store.add_pet(Guppy('Gus'))
store.add_pet(Newt('Tiny'))
store.add_pet(Toucan('Tad'))
store.add_pet(Cat('Kevin'))
store.add_pet(Turtle('Ted'))
store.add_pet(Snake('Slimey'))
store.feed()
print()
store.feature('Tiny')
print("\nReptiles:")
for pet in store.get_reptiles():
    print(pet)
print("\nFish:")
for pet in store.get_fish():
    print(pet)
print("\nAnimals:")
for pet in store.get_by_type(Animal):
    print(pet)
