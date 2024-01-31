from random import choice


class RandomWalk:
    """A class to generate randoms walks."""
    def __init__(self, x_step=-1, y_step=1, num_points=500):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all the points in the walks."""
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Determine the direction and the distance."""
        direction = choice([1, -1])
        distance = choice([0, 1])
        step = direction * distance
        return step
