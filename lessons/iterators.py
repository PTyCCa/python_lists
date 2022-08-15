"""The goal of this exercise is to implement the find_second_index () function. For this exercise, you will need the find_index () function that you implemented in the last exercise. As a reminder, this function returns the index of the first element in the sequence equal to the given value. Find_second_index (), on the other hand, must return the index of the second matching item in the sequence. If there are fewer than two matching elements in the sequence, or if the sequence is empty, you still need to return None."""  # noqa E301


def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index


# BEGIN
def find_second_index(value, items):
    iterator = iter(items)
    first = find_index(value, iterator)
    second = find_index(value, iterator)
    if second is not None:
        return first + second + 1
