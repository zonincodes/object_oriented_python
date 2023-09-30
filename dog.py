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
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """Print a statement showing the car millage"""
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        Check for Positive Integer Values
        """
        if type(miles) == int and miles >= 0:
            self.odometer_reading += miles
        else:
            print("Only Positive Integer Values Allowed")


my_new_car = Car('audi', 'a4', 2016)
my_other_car = Car("Toyota", "Camry", 1964)
my_old_car = Car("Subaru", "Outback", 2020)
my_old_car.update_odometer(20000)
my_old_car.increment_odometer("Hello")
if __name__ == "__main__":
    print(my_dog.name.title())
    print(my_other_car.get_descriptive_name())
    # help(Car)
    my_old_car.read_odometer()
