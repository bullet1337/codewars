# https://www.codewars.com/kata/5b1027fe5b07a105f4000092
from functools import reduce
from operator import mul


def fa(iterable): # iterable, a string or an array
    sum = 0
    last = 1
    for i in range(2, 2 + len(iterable) - 1):
        last *= i
        sum += last
    return sum
        