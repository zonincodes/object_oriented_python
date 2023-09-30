# """Battery Module"""
class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=70):
        """Initialize the battery size"""
        self.battery_size = battery_size
        self.battery_range = 0
        self.charge = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            self.battery_range = 240
            return self.battery_range
        elif self.battery_size == 80:
            self.battery_range = 270

        message = f"This car can go approximately {self.battery_range} miles on full charge"
        print(message)

    def get_distance_remaining(self):
        """Print a statement showing distance remaining"""
        distance = self.battery_range * (self.charge / 100)
        message = f"The battery is {self.charge}% charged. The Remaining distance is {distance} Miles"
        print(message)
