"""Implement the length_of_last_word () function, which returns the length of the last word of a given string. A word is any sequence that does not contain spaces, line feed characters '\' n and tabs '\' t."""  # noqa E301


def length_of_last_word(string):
    words = string.split()
    if not words:
        return 0
    last_word = words[-1]
    return len(last_word)

# Regex version
# import re
#
#
# def length_of_last_word(line):
#    filtered_line = list(filter(None, re.split(r'\s|\n', line)))
#    if len(filtered_line) == 0:
#        return 0
#    return len(filtered_line[len(filtered_line) - 1])
