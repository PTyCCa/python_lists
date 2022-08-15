"""Implement the sum_of_intervals () function that takes a list of intervals as input and returns the sum of all interval lengths. In this problem, only intervals of integers from 1 to ∞ are used, which are presented in the form of lists. The first value in the interval will always be less than the second value. For example, the length of the interval [1, 5] is equal to 4, and the length of the interval [5, 5] is equal to 0. Overlapping intervals should be counted only once."""  # noqa E301


def sum_of_intervals(intervals):
    values = []
    for start, end in intervals:
        for i in range(start, end):
            if i not in values:
                values.append(i)
    return len(values)


# first attempt version
# def sum_of_intervals(list_of_intervals):
#     list_of_intervals.sort()
#     prev_interval = list_of_intervals[0]
#     result = 0
#     for current_interval in list_of_intervals[1:]:
#         if prev_interval[1] > current_interval[0]:
#             prev_interval = [
#                 prev_interval[0], max(prev_interval[1], current_interval[1]),
#             ]
#         else:
#             result += prev_interval[1] - prev_interval[0]
#             prev_interval = current_interval
#     result += prev_interval[1] - prev_interval[0]
#     return result
