"""To successfully complete this practice, you will need to implement two functions:

get_square_roots
This function should take a number and return a list of the square roots of that number. For example, for argument 9, the function should return [-3, 3]. The test expects the negative root to appear first, if any. Also, there can be one root if the argument is zero. Also, there may be no roots if the argument is negative.

get_range
This function must, for a given positive number of the argument n, return a list of numbers from zero to n, not including the number n itself. If a negative number or zero was passed in the call, the function should return an empty list."""  # noqa E301
import math


def get_square_roots(argument):
    if argument < 0:
        return []
    elif argument:
        root = math.sqrt(argument)
        return [-root, root]
    return [0]


def get_range(up_to):
    result = []
    counter = 0
    while counter < up_to:
        result.append(counter)
        counter += 1
    return result
