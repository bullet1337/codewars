# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
import operator
from functools import reduce


def persistence(n, k=0):
    if n < 10:
        return k
    else:
        return persistence(reduce(operator.mul, (int(d) for d in str(n))), k + 1)