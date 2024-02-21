

class Restaurant:
    """"""
    def __init__(self, restaurant_name, cuisine_type):
        """initiate a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 8

    def describe_restaurant(self):
        """Print a description of the restaurant"""
        print(f"This is {self.restaurant_name} and the cuisine type is {self.cuisine_type}!")

    def open_restaurant(self):
        """Prints a message indicating it is open."""
        print(f"{self.restaurant_name} is open now!")

    def set_number_served(self, number_served):
        """set the number of served"""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increment the number of served"""
        self.number_served += number_served
        print(f"{self.number_served} have been served today!")


restaurant = Restaurant("new_one", "do not know")
restaurant.set_number_served(2)
restaurant.increment_number_served(2)
