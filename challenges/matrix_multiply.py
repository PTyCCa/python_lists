"""The operation of multiplying two matrices A and B is the calculation of the resulting matrix C, where each element C (ij) is equal to the sum of the products of the elements in the corresponding row of the first matrix A (ik) and the elements in the column of the second matrix B (kj).

Two matrices can be multiplied only if the number of columns in the first matrix is ​​the same as the number of rows in the second matrix. This means that the first matrix must be consistent with the second matrix. As a result of the operation of multiplying an M × N matrix by an N × K matrix, an M × K matrix is ​​obtained.

Implement a multiply () function that takes two matrices and returns a new matrix that is the result of their product."""  # noqa E301


def zero_matrix(rows, columns):
    matrix = []
    row = [0] * columns
    for _ in range(rows):
        matrix.append(row[:])
    return matrix


def multiply(a, b):  # noqa: WPS210
    rows_in_a = len(a)
    columns_in_b = len(b[0])
    c = zero_matrix(rows_in_a, columns_in_b)
    for row_a, row_c in zip(a, c):
        for x in range(columns_in_b):
            for y, row_b in enumerate(b):
                row_c[x] += row_a[y] * row_b[x]
    return c


# alternative old version
#
#
# def multiply(first_matrix, second_matrix):
#     if len(first_matrix) != len(second_matrix[0]):
#         print(
#             'ОШИБКА!\nМатрица должна быть согласованной\n')
#     return [[
#               sum(x * y for x, y in zip(X_row,Y_col)) for
#               Y_col in zip(*second_matrix)] for
#               X_row in first_matrix,
# ]
# END
