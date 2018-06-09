# https://www.codewars.com/kata/554b4ac871d6813a03000035
from operator import itemgetter


def high_and_low(numbers):
    return '{} {}'.format(*itemgetter(-1, 0)(sorted(int(x) for x in numbers.split())))