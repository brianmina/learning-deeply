from random import choice


class Die:
    """gives a random number between two integers."""

    def __init__(self, num=6):
        """Initialize the die with six sides"""
        self.sides = num

    def roll_die(self):
        """Roll the six-sided die."""
        die_rolled = choice([0, 1, 2, 3, 4, 5, 6])
        return die_rolled


attempt_1 = Die(6)
for num_rolls in range(0, 10):
    """Roll the die 10 times"""
    times_rolls = attempt_1.roll_die()
    print(times_rolls)

