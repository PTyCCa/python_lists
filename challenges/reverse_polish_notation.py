"""In this exercise, you need to implement a stacking machine, that is, an algorithm that performs calculations based on reverse Polish notation.

Reverse Polish notation or postfix notation is a form of writing mathematical and logical expressions in which the operands are placed before the operation signs. The expression is read from left to right. When an operation sign is encountered in an expression, the corresponding operation is performed on the two nearest operands to the left of the operation sign. The result of the operation replaces the sequence of its operands and the sign in the expression, after which the expression is evaluated further according to the same rule. Thus, the result of evaluating the entire expression is the result of the last evaluated operation.

For example, the expression (1 + 2) * 4 + 3 in postfix notation will look like this: 1 2 + 4 * 3 +, and the result of the calculation is 15. Another example is the expression: 7 - 2 * 3, in postfix notation: 7 2 3 * -, result: 1.

Implement the rpn_calc function, which takes a list, each element of which contains a number or an operation sign (+, -, *, /). The function should return the result of the calculation using the reverse polish notation."""  # noqa E301

import operator


get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}.get


def rpn_calc(rpn):
    stack = []
    for elem in rpn:
        op = get_operator(elem)
        if op is not None:
            x = stack.pop()
            y = stack.pop()
            elem = op(y, x)
        stack.append(elem)
    return stack[0]


# first version
def rpn_calc_ver1(expression):
    """Enter RPN and get result."""
    operators = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a / b),
    }
    operands = ''.join(str(x) for x in expression)
    stack = []

    for token in operands:
        if token in operators:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = operators.get(token)(arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()
