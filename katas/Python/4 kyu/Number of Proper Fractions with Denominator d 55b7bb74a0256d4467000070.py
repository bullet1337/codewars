# https://www.codewars.com/kata/55b7bb74a0256d4467000070
import itertools
import operator
from functools import reduce
from math import sqrt, ceil


def get_dividers(n):
    dividers = set()
    while n > 1:
        found = False
        for i in range(2, int(ceil(sqrt(n))) + 1):
            if i not in dividers and any(i % divider == 0 for divider in dividers):
                continue

            div, mod = divmod(n, i)
            if mod == 0:
                dividers.add(i)
                n = div
                found = True
                break
        if not found:
            dividers.add(n)
            break
    return dividers


def proper_fractions(n):
    if n == 1:
        return 0

    dividers = get_dividers(n)
    sum = 0
    sign = 1
    for i in range(1, len(dividers) + 1):
        for tuple in itertools.combinations(dividers, i):
            sum += sign * n // reduce(operator.mul, tuple)
        sign = -sign
    return n - sum