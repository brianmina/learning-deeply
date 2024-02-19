


class Employee:
    """Information about the employee."""
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the Employee object."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, new_raise=5000):
        """Add a new raise."""
        self.annual_salary += new_raise
