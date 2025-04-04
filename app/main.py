class Animal:
    animals = []
    def __init__(self, name: str, appetite: int, is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.animals.append(self)

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")
    # feed() should print Eating {appetite} food points...,
    # set is_hungry to False and return number of eaten food points if animal is hungry.
    # Otherwise, it should return 0 and print nothing
    def feed(self):
        self.hunger()
        if self.appetite:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            return self.appetite
        else:
            return 0
    def hunger(self):
        if not self.is_hungry:
            self.appetite = 0

def feed_animals(list_of_animals: list):
    appetite = 0
    for animal in Animal.animals:
        if animal in list_of_animals:
            animal.hunger()
            appetite += animal.appetite

    return appetite



class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self):
        print("The hunt began!")

class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")
