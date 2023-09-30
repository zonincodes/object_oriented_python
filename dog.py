# Simple Dog class
class Dog:
    """ A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age Attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over on response to command"""
        print(self.name.title() + " rolled over!")


my_dog = Dog("rex", 10)


class Car:
    """Initialize attributes to describe a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
my_other_car = Car("Toyota", "Camry", 1964)

if __name__ == "__main__":
    print(my_dog.name.title())
    print(my_other_car.get_descriptive_name())