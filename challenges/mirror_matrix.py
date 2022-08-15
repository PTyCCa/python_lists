"""Implement mirror_matrix (), which takes a two-dimensional list (matrix) and modifies it (in place) so that the right half of the matrix becomes a mirror copy of the left half, symmetrical about the vertical axis of the matrix. If the width of the matrix is odd, then the "middle" column should not be affected."""  # noqa E301


def mirror_matrix(matrix):
    if matrix:
        half_len = len(matrix[0]) // 2
        for line in matrix:
            line[half_len:] = line[-half_len - 1::-1]
# END
