class User:
    """information about the user."""
    def __init__(self, first_name, last_name, nationality):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality

    def describe_user(self):
        """Prints a summary of the user's information."""
        user_info = f"Full name: {self.first_name} {self.last_name} \nNationality: {self.nationality}"
        print(user_info)

    def greet_user(self):
        """Prints a personalized message."""
        print(f"Hey,{self.first_name}! \n")

user_1 = User("Brian", "Mina", "Colombian")
user_2 = User("Karl", "Marx-Levi", "American")

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
