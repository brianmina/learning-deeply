

class Restaurant:
    """"""
    def __init__(self, restaurant_name, cuisine_type):
        """initiate a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a description of the restaurant"""
        print(f"This is {self.restaurant_name} and the cuisine type is {self.cuisine_type}!")

    def open_restaurant(self):
        """Prints a message indicating it is open."""
        print(f"{self.restaurant_name} is open now!")


restaurant = Restaurant("Yard House", "American")
new_restaurant = Restaurant("mexicalli", "mexican")
old_restaurant = Restaurant("colombian", "colombian")

new_restaurant.describe_restaurant()
old_restaurant.describe_restaurant()
restaurant.describe_restaurant()
restaurant.open_restaurant()
