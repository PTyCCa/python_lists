"""In this exercise, you will implement a classic search loop. The find_index () function that you are going to write must take a value and something that can be iterated over - a string, a list, a tuple. In response, the function should return the index of the first element of the iterated sequence, equal to the specified value. If there is no value in the sequence, or if the sequence is empty, the function must return None."""  # noqa E301


def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index
