# https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc
from collections import Counter

import itertools


def solve(arr):
    return list(itertools.chain(*([k] * v for k, v in
                                  sorted(Counter(arr).items(), key=lambda e: (e[1], -e[0]), reverse=True))))