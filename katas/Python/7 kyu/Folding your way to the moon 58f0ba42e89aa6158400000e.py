# https://www.codewars.com/kata/58f0ba42e89aa6158400000e
from math import log2, ceil


def fold_to(distance):
    return None if distance < 0 else ceil(log2(max(distance * 1e4, 1)))