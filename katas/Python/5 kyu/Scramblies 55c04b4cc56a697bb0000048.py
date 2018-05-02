# https://www.codewars.com/kata/55c04b4cc56a697bb0000048
from collections import Counter


def scramble(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    return all(c1[l] >= c for l, c in c2.items())