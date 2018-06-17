# https://www.codewars.com/kata/528e95af53dcdb40b5000171
from functools import reduce
from operator import mul


def factorial(n):
    return reduce(mul, range(1, n + 1), 1) if n >= 0 else None