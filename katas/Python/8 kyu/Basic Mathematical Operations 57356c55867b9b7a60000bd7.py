# https://www.codewars.com/kata/57356c55867b9b7a60000bd7
from operator import add, sub, mul, truediv

ops = {'+': add, '-': sub, '*': mul, '/': truediv}


def basic_op(operator, value1, value2):
    return ops[operator](value1, value2)
        