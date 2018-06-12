# https://www.codewars.com/kata/537baa6f8f4b300b5900106c
from math import pi


def circleArea(r):
    return round(pi * r ** 2, 2) if isinstance(r, int) and r > 0 else False