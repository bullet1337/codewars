# https://www.codewars.com/kata/5a942c461a60f677730032df
import re

import itertools


def check_order(t):
    for i in range(1, len(t)):
        if t[i] <= t[i - 1]:
            return False
    return True


def solve(a, b):
    indices = ((m.start() for m in re.finditer(c, b)) for c in a)
    return len([t for t in itertools.product(*indices) if check_order(t)])