# https://www.codewars.com/kata/59da47fa27ee00a8b90000b4
import itertools

odds = {'1', '3', '5', '7', '9'}


def solve(s):
    return sum(1 for _, j in itertools.combinations(range(len(s) + 1), 2) if s[j - 1] in odds)