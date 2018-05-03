# https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0
from math import log


def whoIsNext(names, r):
    i = int(log(1 + r / len(names), 2))
    return names[(r - 1 + len(names) * (1 - 2 ** i)) // 2 ** i]