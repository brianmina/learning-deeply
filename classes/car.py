class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model,  year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 900

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ Prints the current mileage of the car
        Reject rolling it back."""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back the odometer.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""

        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("You can not roll back the odometer.")


my_car = Car("Audi", "A4", 2009 )
print(my_car.get_descriptive_name())


my_car.update_odometer(900)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()

my_car.increment_odometer(-50)
my_car.read_odometer()

