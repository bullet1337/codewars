# https://www.codewars.com/kata/54d4c8b08776e4ad92000835
from math import sqrt, log


def isPP(n):
    for i in range(2, round(sqrt(n)) + 1):
        log_i = log(n, i)
        if abs(log_i - round(log_i)) < 1e-9:
            return [i, round(log_i)]
    return None