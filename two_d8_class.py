from random import randint


class Die:
    """A class that represents a die."""
    def __init__(self, num_sides=8):
        """Assume the die is a eigth-side die."""
        self.num_sides = num_sides

    def roll(self):
        """Return the value between 1 and 8."""
        result = randint(1, self.num_sides)
        return result
