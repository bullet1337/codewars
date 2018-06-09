# https://www.codewars.com/kata/563b662a59afc2b5120000c6
from itertools import repeat, accumulate, takewhile


def nb_year(p0, percent, aug, p):
    return len(list(takewhile(lambda x: x < p, accumulate(repeat(p0), lambda a, b: int(a * (1 + percent / 100) + aug)))))