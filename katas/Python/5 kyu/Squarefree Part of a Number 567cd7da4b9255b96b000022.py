# https://www.codewars.com/kata/567cd7da4b9255b96b000022
import operator
from functools import reduce
from math import ceil, sqrt



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


def square_free_part(n):
    if not isinstance(n, int):
        return None

    dividers = get_dividers(n)
    if len(dividers) == 0:
        return None

    return reduce(operator.mul, dividers)