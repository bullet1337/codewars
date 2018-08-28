# https://www.codewars.com/kata/55eeddff3f64c954c2000059
from itertools import groupby


def sum_consecutives(s):
    return [sum(g) for _, g in groupby(s)]