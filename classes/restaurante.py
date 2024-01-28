class Restaurant:
    """Simple information of a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 1

    def describe_restaurant(self):
        """Describe name and type of cuisine."""
        print(f"This restaurant is called {self.name} and makes {self.cuisine_type}")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print(f"{self.name} is now open!.")

    def set_number_served(self, num_served):
        """Set the number of customers served"""
        self.number_served = num_served

    def increment_number_served(self, new_num_served):
        "print the new number of customers served"
        self.number_served += new_num_served
        print(f"Number of serverd: {self.number_served}")


restaurant = Restaurant('Mexicali', "pizza")
print(restaurant.number_served)

restaurant.set_number_served(5)
restaurant.increment_number_served(9)
restaurant.increment_number_served(9)