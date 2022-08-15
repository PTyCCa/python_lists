"""Implement the find_longest_length () function that takes a string as input and returns the length of the maximum sequence of non-repeating characters. A substring can be one character. For example, in the qweqrty line, you can select the following substrings: qwe, weqrty. The longest will be weqrty, and its length is 6 characters."""  # noqa E301


def unique_sequence_length(string):
    unique_sequence = set()
    length = 0
    for char in string:
        if char in unique_sequence:
            break
        unique_sequence.add(char)
        length += 1
    return length


def find_longest_length(string):
    longest_length = 0
    for i, _ in enumerate(string):
        substring_length = unique_sequence_length(string[i:])
        if longest_length < substring_length:
            longest_length = substring_length
    return longest_length
