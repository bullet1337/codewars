# https://www.codewars.com/kata/5254ca2719453dcc0b00027d
from itertools import permutations as p


def permutations(string):
    return list(''.join(x) for x in set(p(string)))