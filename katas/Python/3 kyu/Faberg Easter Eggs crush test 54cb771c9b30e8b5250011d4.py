# https://www.codewars.com/kata/54cb771c9b30e8b5250011d4
from itertools import accumulate, chain


def height(n, m):
    if m == 0 or n == 0:
        return 0

    return sum(accumulate(chain([1], range(1, n + 1)), lambda coef, i: coef * (m - i + 1) // i)) - 1
