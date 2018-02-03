# https://www.codewars.com/kata/5a71939d373c2e634200008e
from functools import reduce


def solve(s):
    ws = s.replace(' ', '')
    return reduce(lambda x, e: x + ws[-1 - len(x) + e[0]:-1 + e[0] - e[1]:-1] + ' ',
                  enumerate(i for i, c in enumerate(s + ' ') if c == ' '), '')[:-1]