"""Pascal's triangle is an infinite table of binomial coefficients that has a triangular shape. In this triangle, there are ones at the top and on the sides. Each number is equal to the sum of the two numbers above it. The lines of the triangle are symmetrical about the vertical axis.

Write a triangle () function that returns the specified Pascal triangle string as a list."""  # noqa E301


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def triangle(row_number):
    numbers_count = row_number + 1
    line = []
    for i in range(numbers_count):
        # Для вычисления числа заданной строки используем формулу
        # расчёта биноминальных коэффициентов С(n, k) = n! / (k! * (n - k)!)
        line.append(fact(row_number) / (fact(i) * fact(row_number - i)))
    return line

# Alternative solution
#
#
# def triangle(row):
#     line = [1]
#     for i in range(row):
#         line.append(line[i] * ((row - i) / (i + 1)))
#     return line
#
#
# from operator import add
#
#
# def triangle(row_number):
#     row = [1]
#     for _ in range(row_number):
#         row = list(map(  # [x,y,z]
#             add,         # x y z 0
#             row + [0],   # + + + +
#             [0] + row,   # 0 x y z
#         ))
#     return row

# Alternative solution 2
#
#
# def triangle(n):
#    line = []
#    for _ in range(n + 1):
#        line_length = len(line)
#        line = [1 if i == 0 or i == line_length
#                else line[i - 1] + line[i]
#                    for i in range(line_length + 1)]
#    return line
