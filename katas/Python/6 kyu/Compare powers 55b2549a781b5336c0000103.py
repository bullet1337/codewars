# https://www.codewars.com/kata/55b2549a781b5336c0000103
from math import log


def compare_powers(n1, n2):
    def sign(x):
        return 1 if x > 0 else -1 if x < 0 else 0
    return sign(log(n2[0], n1[0]) * n2[1] - n1[1] if n1[0] != 1 else n2[0] - n1[0])