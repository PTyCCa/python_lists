"""You need to implement the duplicate () function, which should take a list as an argument and double the list in place (you will need to modify the original list object. Remember: the list is passed by reference!). Doubling here means that after the function is applied to it, the list should have a copy of all elements appended to the end."""  # noqa E301


def duplicate(items):
    items.extend(items)
