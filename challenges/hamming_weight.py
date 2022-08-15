"""Implement the hamming_weight function that calculates the Hamming weight."""  # noqa E301


def hamming_weight(number):
    weight = 0
    digits = bin(number)[2:]

    for num in digits:
        weight += int(num)

    return weight

# Alternative solutions
# def hamming_weight(x):
#     s = 0
#     while x:
#         x, r = divmod(x, 2)
#         s += r
#     return s


# def hamming_weight(number):
#     return bin(number).count('1')
# END
