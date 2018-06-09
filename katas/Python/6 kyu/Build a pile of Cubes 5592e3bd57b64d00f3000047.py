# https://www.codewars.com/kata/5592e3bd57b64d00f3000047
from itertools import count, accumulate, takewhile


def find_nb(m):
    x = list(takewhile(lambda x: x <= m, accumulate(x ** 3 for x in count(1))))
    return -1 if x[-1] != m else len(x)