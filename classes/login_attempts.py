class User:
    """information about the user."""
    def __init__(self, first_name, last_name, e_mail, nationality):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.nationality = nationality
        self.login_attempt = 0

    def describe_user(self):
        """Prints a summary of the user's information."""
        user_info = f"Full name: {self.first_name} {self.last_name} \nNationality: {self.nationality}"
        print(user_info)

    def greet_user(self):
        """Prints a personalized message."""
        print(f"Hey,{self.first_name}! \n")

    def increment_login_attempt(self, attempts):
        """Increment the value of logins in every attempt."""
        self.login_attempt += attempts
        print(f"\tNumber of attempts: {self.login_attempt}")

    def reset_login_attempts(self):
        """Reset the login attempts number."""
        self.login_attempt = 0
        print("\tLOGIN ATTEMPTS RESETED!")


user_1 = User("Brian", "Mina", "bdmina@example.com", "Colombian")
user_1.describe_user()
user_1.greet_user()

print("\nMaking attempts:")
user_1.increment_login_attempt(6)
user_1.increment_login_attempt(5)
user_1.increment_login_attempt(9)

print("\nResseting attempts...")
user_1.reset_login_attempts()

print(user_1.login_attempt)