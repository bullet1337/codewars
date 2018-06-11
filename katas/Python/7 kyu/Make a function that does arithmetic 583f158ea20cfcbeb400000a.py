# https://www.codewars.com/kata/583f158ea20cfcbeb400000a
from operator import add, sub, mul, truediv


ops = {'add': add, 'subtract': sub, 'divide': truediv, 'multiply': mul}


def arithmetic(a, b, op):
    return ops[op](a, b)