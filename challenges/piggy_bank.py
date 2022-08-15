"""Implement the visualize () function that calculates how many coins of each denomination are in the piggy bank and displays the result in the form of a graph. Each column of the chart is a stack of coins of a certain denomination.

For simplicity, let's agree that there are always coins in the piggy bank, and their number is not limited, and the denomination can be any.

The function accepts a list or a tuple of numbers as input and returns a graph as a string. The optional argument bar_char specifies the character with which to draw the chart. The default is the ruble sign (₽)."""  # noqa E301

from collections import Counter


def visualize(coins, bar_char='₽'):  # noqa: WPS210
    """Visualize money in a money box."""
    # BEGIN
    counts = Counter(coins)
    nominals = sorted(counts.keys())
    highest_stack = max(counts.values())

    rows = []
    delimiter = ''

    for level in range(highest_stack, -1, -1):
        row = ''
        for _, bar in sorted(counts.items()):
            if bar > level:
                row += '{} '.format(bar_char * 2)
            elif bar == level and bar != 0:
                row += '{:<2d} '.format(bar)
                delimiter += '---'
            else:
                row += '   '
        rows.append(row[:-1])

    rows.append(delimiter[:-1])
    row = ''
    for nominal in nominals:
        row += '{:<2d} '.format(nominal)
    rows.append(row[:-1])

    return '\n'.join(rows)


# first try
def visualize_old(coins, bar_char='₽'):  # noqa: WPS210
    """Visualize money in a money box."""
    # BEGIN (write your solution here)
    vc = Counter()
    for coin in coins:
        vc[coin] += 1
    sorted_coin_denom = dict(enumerate(sorted(vc.keys())))
    matrix_graph = []
    for i in range(max(vc.values()) + 1):
        matrix_graph.append([0] * len(vc.keys()))
    for i, den in sorted_coin_denom.items():
        for de, s in vc.items():
            if den == de:
                matrix_graph[abs(max(vc.values()) - s)][i] = s
    matrix_width = len(vc.keys())
    first = 0
    for i in range(matrix_width):
        for row in matrix_graph:
            if row[i] == first:
                row[i] = '  '
            elif row[i] > first:
                first = row[i]
                row[i] = str(row[i]) + " "
            elif row[i] < first:
                row[i] = bar_char * 2
        first = 0
    result_string = ''
    dot_line = ''
    for i in matrix_graph:
        dot_line = len(' '.join(i)) * '-'
        result_string += ' '.join(i) + '\n'
    result_string += dot_line + '\n'
    end = list(str(x) for x in sorted_coin_denom.values())
    formated_last_string = []
    for i in end:
        if len(i) < 2:
            formated_last_string.append(i + ' ')
        else:
            formated_last_string.append(i)
    result_string += ' '.join(formated_last_string)
    return result_string
