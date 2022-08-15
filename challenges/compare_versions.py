"""Implement the compare_version () function that compares the passed versions: version1 and version2. If version1> version2, then the function should return 1, if version1 <version2, then -1, if version1 = version2 - 0.

A version is a string in which two numbers (major and minor versions) are separated by a dot, for example: 12.11. It is important to understand that a version is not a floating point number, but several unrelated numbers. Checking for more / less is performed by comparing each number independently. Therefore, version 0.12 is greater than version 0.2."""  # noqa E301


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def compare_version(first, second):
    [a1, b1] = first.split('.')
    [a2, b2] = second.split('.')

    major = sign(int(a1) - int(a2))
    minor = sign(int(b1) - int(b2))

    return major if major != 0 else minor
