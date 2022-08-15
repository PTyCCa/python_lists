"""Implement a transposed () function that should take a matrix as a list of lists and return a transposed matrix (a new list of lists).

Keep in mind that even though strictly square matrices are transposed in mathematics, your transposed () function should be more "omnivorous": it should be able to flip rectangular matrices too!"""  # noqa #301


def transposed(matrix):
    return list(map(list, zip(*matrix)))
