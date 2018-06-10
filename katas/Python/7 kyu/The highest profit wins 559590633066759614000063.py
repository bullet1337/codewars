# https://www.codewars.com/kata/559590633066759614000063
from operator import itemgetter


def min_max(lst):
    return list(itemgetter(0, -1)(sorted(lst)))