# https://www.codewars.com/kata/56269eb78ad2e4ced1000013
from math import sqrt


def find_next_square(sq):
    sq = sqrt(sq)
    return (sq + 1) ** 2 if abs(sq - int(sq)) < 1e-9 else -1
