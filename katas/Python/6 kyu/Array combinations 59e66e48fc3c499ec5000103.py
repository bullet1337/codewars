# https://www.codewars.com/kata/59e66e48fc3c499ec5000103
from functools import reduce
from operator import mul


def solve(arr):
    return reduce(mul, (len(set(x)) for x in arr))