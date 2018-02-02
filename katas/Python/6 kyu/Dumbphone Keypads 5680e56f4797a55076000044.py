# https://www.codewars.com/kata/5680e56f4797a55076000044
from functools import reduce

symbols_groups = ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', '*', ' 0', '#']
symbols_map = {c: group[-1] * (i + 1) for group in symbols_groups for i, c in enumerate(group)}


def sequence(phrase):
    return reduce(lambda a, b: a + ('p' if a[-1] == b[0] else '') + b, (symbols_map[c.upper()] for c in phrase))