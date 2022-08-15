"""Implement the snail_path () function that takes a matrix as input and returns a list of matrix elements in order from the top-left element clockwise to the innermost one. Movement across the matrix resembles a snail."""  # noqa E301


def rotate(matrix):
    """
    Rotate the matrix counter-clockwise.

    >>> rotate([[1]])
    [(1,)]
    >>> rotate([[1, 2, 3]])
    [(3,), (2,), (1,)]
    >>> rotate([[1, 2], [3, 4]])
    [(2, 4), (1, 3)]
    """
    return list(reversed(list(zip(*matrix))))


def snail_path(matrix):
    path = []

    def trace(submatrix):
        if not submatrix:
            return
        path.extend(submatrix[0])
        trace(rotate(submatrix[1:]))
    trace(matrix)
    return path

# old version
#
# def snail_path(matrix):
#     if not matrix:
#         return
#
#     result = []
#     row_start = 0
#     row_end = len(matrix) - 1
#     col_start = 0
#     col_end = len(matrix[0]) - 1
#
#     while row_start <= row_end and col_start <= col_end:
#         for i in range(col_start, col_end + 1):
#             result.append(matrix[row_start][i])
#         row_start += 1
#
#         for i in range(row_start, row_end + 1):
#             result.append(matrix[i][col_end])
#         col_end -= 1
#
#         if row_start <= row_end:
#             for i in range(col_end, col_start - 1, -1):
#                 result.append(matrix[row_end][i])
#         row_end -= 1
#
#         if col_start <= col_end:
#             for i in range(row_end, row_start - 1, -1):
#                 result.append(matrix[i][col_start])
#         col_start += 1
#
#     return result
