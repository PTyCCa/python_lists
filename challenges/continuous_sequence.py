"""Implement the is_continuous_sequence () function, which checks if the passed sequence of integers is continuously increasing (no gaps). For example, the sequence [4, 5, 6, 7] is continuous, but [0, 1, 3] is not. The sequence can start with any number. The main condition is the absence of missing numbers. A sequence of one number cannot be considered ascending."""  # noqa E301


def is_continuous_sequence(source):
    if len(source) < 2:
        return False
    for x, y in zip(source, source[1:]):
        if (y - x) != 1:
            return False
    return True

# First variant
# def is_continuous_sequence(sequence):
#    if len(sequence) < 2:
#        return False
#    sort_seq = list(
#                    range(sorted(sequence)[0], sorted(
#                                                      sequence)[len(sequence)-1]+1))
#    return sequence == sort_seq
