"""Implement summary_ranges (), which finds contiguous ascending sequences of numbers in a list and returns a list listing them."""  # noqa E301


def summary_ranges(numbers):
    if not numbers:
        return []

    ranges = []
    current_sequence = [numbers[0]]
    sequences = [current_sequence]

    for x, y in zip(numbers, numbers[1:]):
        if (y - x) == 1:
            current_sequence.append(y)
        else:
            current_sequence = [y]
            sequences.append(current_sequence)

    for sequence in sequences:
        if len(sequence) > 1:
            first, last = sequence[0], sequence[-1]
            ranges.append('{}->{}'.format(first, last))

    return ranges
