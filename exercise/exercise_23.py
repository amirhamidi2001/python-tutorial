import copy
import random


class Hat:
    """A hat that contains balls of different colors and allows random draws."""

    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """
        Draw `num_balls` random balls from the hat.
        If num_balls exceeds available balls, return all balls.
        """
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls

        drawn_balls = []
        for _ in range(num_balls):
            index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(index))

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Run Monte Carlo experiments by drawing balls from a hat.
    Returns probability of drawing at least the expected number of balls.
    """
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        success = True
        for color, expected_count in expected_balls.items():
            if drawn_counts.get(color, 0) < expected_count:
                success = False
                break

        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments
