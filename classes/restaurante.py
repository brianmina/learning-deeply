class Restaurant:
    """Simple information of a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe name and type of cuisine."""
        print(f"This restaurant is called {self.name} and makes {self.cuisine_type}")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print(f"{self.name} is now open!.")


my_restaurant = Restaurant('Mexicali', "pizza")
your_restaurant = Restaurant("Italiano", "burgers")
our_restaurant = Restaurant("Le Americano", "arepas")

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
our_restaurant.describe_restaurant()