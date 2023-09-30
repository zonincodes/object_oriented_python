# imports
from dog import Dog
from car import Car
from electric_car import ElectricCar

my_dog = Dog("rex", 10)
my_new_car = Car('audi', 'a4', 2016)
my_other_car = Car("Toyota", "Camry", 1964)
my_old_car = Car("Subaru", "Outback", 2020)
my_old_car.update_odometer(20000)
my_old_car.increment_odometer("Hello")
my_tesla = ElectricCar('tesla', 'model s', 2016)

if __name__ == "__main__":
    print(my_dog.name.title())
    print(my_other_car.get_descriptive_name())
    # help(Car)
    my_old_car.read_odometer()
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    my_tesla.battery.get_distance_remaining()
    help(Car.get_descriptive_name)
