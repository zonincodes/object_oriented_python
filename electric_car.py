# Imports
from car import Car
from battery import Battery


# inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
