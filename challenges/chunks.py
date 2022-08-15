"""Implement a chunked function that takes a number and a sequence as input. The number specifies the size of the chunk (chunk). The function should return a list consisting of chunks of the specified dimension. In this case, the list should be divided into pieces-lists, a line - into lines, a tuple - into tuples!"""  # noqa E301


def chunked(size, source):
    result = []
    index = 0
    while index < len(source):
        result.append(source[index:index + size])
        index += size
    return result
