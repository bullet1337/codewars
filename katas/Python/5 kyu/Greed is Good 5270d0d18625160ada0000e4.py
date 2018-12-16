# https://www.codewars.com/kata/5270d0d18625160ada0000e4
from collections import Counter  


def score(dice):
    сounter = Counter(dice)
    s = 0
    for v, c in сounter.items():
        if c >= 3:
            s += (v if v > 1 else 10) * 100
        if v in [1, 5]:
            s += (c % 3) * (v if v > 1 else 10) * 10
    return s