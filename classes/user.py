

class User:
    def __init__(self, first_name, last_name):
        """Initialize the User object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = ""
        self.email = ""
        self.phone_number = ""
        self.birth_date = ""

    def describe_user(self):
        """prints a message with the user information."""
        print(f"Name: {self.first_name}, {self.last_name}."
              f"\nAge: {self.age}\nEmail: {self.email},\nPhone Number: {self.phone_number},\nBirth Date: {self.birth_date}")

    def greet_user(self):
        """Prints a message greeting to the user"""
        print(f"Hello, {self.first_name}")


user_1 = User("John", "Doe")
user_1.describe_user()
user_1.greet_user()