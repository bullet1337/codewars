# https://www.codewars.com/kata/52f78966747862fc9a0009ae
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def calc(expr):
    if not expr:
        return 0

    stack = []
    for arg in expr.split():
        if arg in operators:
            arg2, arg1 = stack.pop(), stack.pop()
            stack.append(operators[arg](arg1, arg2))
        else:
            stack.append(float(arg))
    return stack[-1]