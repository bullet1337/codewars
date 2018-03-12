# https://www.codewars.com/kata/59daf400beec9780a9000045
import re

import itertools


def check_order(t):
    for i in range(1, len(t)):
        if t[i] <= t[i - 1]:
            return False
    return True


def name_in_str(a, b):
    a = a.lower()
    b = b.lower()
    indices = ((m.start() for m in re.finditer(c, a)) for c in b)
    return len([t for t in itertools.product(*indices) if check_order(t)]) > 0