import random
import math
from math import *

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr1 = lambda x, y: (x + y)/2 - (x - y)
    expr2 = lambda x, y: (x - y)/2 + (x + y)
    expr3 = lambda x, y: ((pi * sin(x) - pi * sin(y)))
    expr4 = lambda x, y: (x - y)/2 * random.random
    return random.choice([expr1, expr2, expr3, expr4])


# alternate example
    # res =[]
    #
    # for _ in range(random.randint(1, 5)):
    #     res.append(random.choice(['sin', 'cos', 'tan']) + random.choice(['(x)', '(y)'])
    #
    # print('*'.join)


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
