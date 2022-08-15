"""In this exercise, you will need to implement two functions, rotated_left () and rotated_right (). Each function must

accept a list, tuple, or string as an argument,
get a new value of the same type using slices and concatenation,
return this value.
The functions differ only in "direction of rotation" (see examples below).

Because both strings and lists with tuples allow concatenation and slicing, your code does not need to check the argument type - you only need to do with slices and concatenation!

Please note: function names contain a verb with the ending ed - in Python, functions that return a new value based on the old one are often called in this way.

When rotated to the left, the first element moves to the end.

When rotated to the right, the last element moves to the beginning."""  # noqa E301


def rotated_right(items):
    return items[-1:] + items[:-1]


def rotated_left(items):
    return items[1:] + items[:1]
