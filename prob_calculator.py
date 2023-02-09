######
### freeCodeCamp
### Scientific Computing with Python Projects
### Probability Calculator
### https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator
######

# First, create a Hat class in prob_calculator.py.
# The class should take a variable number of arguments that specify the number of balls of each color that are in the hat.
# A hat will always be created with at least one ball.
# The arguments passed into the hat object upon creation should be converted to a contents instance variable.
# contents should be a list of strings containing one item for each ball in the hat.
# Each item in the list should be a color name representing a single ball of that color.


import random
import copy


class Hat:
    def __init__(self, **balls):
        self.balls = balls
        contents = []
        for key, value in self.balls.items():
            for _ in range(value):
                contents.append(key)
        self.contents = contents

    def __str__(self):
        return f"{self.balls} {self.contents}"

    # The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat.
    # This method should remove balls at random from contents and return those balls as a list of strings.
    # The balls should not go back into the hat during the draw, similar to an urn experiment without replacement.
    # If the number of balls to draw exceeds the available quantity, return all the balls.

    def draw(self, number_of_balls_to_draw):
        self.draw_list = []  # list of drawn balls
        if number_of_balls_to_draw > len(self.contents):
            return self.contents

        for _ in range(number_of_balls_to_draw):
            x = random.choice(self.contents)
            self.draw_list.append(x)
            self.contents.remove(x)
        return self.draw_list


###
# Next, create an experiment function in prob_calculator.py (not inside the Hat class). 
# This function should accept the following arguments:

# hat: A hat object containing balls that should be copied inside the function.
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. 
# For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, 
# set expected_balls to {"blue":2, "red":1}.
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.
# num_experiments: The number of experiments to perform. 
# (The more experiments performed, the more accurate the approximate probability will be.)
# The experiment function should return a probability.
###


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0  # number of correct draws
    exp_balls_list = []  # list of expected balls
    draw_list = []  # list of drawn balls (return form def draw)
    hat_copy = copy.deepcopy(hat)  # hat copy

    for key, value in expected_balls.items():
        for _ in range(value):
            exp_balls_list.append(key)

    for _ in range(num_experiments):
        draw_list = hat.draw(num_balls_drawn)
        hat = copy.deepcopy(hat_copy)
        try:
            for ball in exp_balls_list:
                draw_list.remove(ball)

        except ValueError:
            pass

        else:
            count += 1

    return count / num_experiments


###
## EXAMPLES
###

#### 1

hat = Hat(yellow=5, blue=2, red=1)
probability = experiment(hat = hat,expected_balls={"yellow":1,"red":1}, num_balls_drawn=4,
                  num_experiments=10000)

print(probability)

#### 2

# hat = Hat(black=6, red=4, green=3)
# probability = experiment(hat=hat,
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=100)

# print(probability)
