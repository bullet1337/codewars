# https://www.codewars.com/kata/5250a89b1625e5decd000413
from itertools import chain


def flatten(lst):
    return list(chain.from_iterable(x if isinstance(x, list) else [x] for x in lst))