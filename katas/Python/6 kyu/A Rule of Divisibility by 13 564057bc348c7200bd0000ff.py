# https://www.codewars.com/kata/564057bc348c7200bd0000ff
from itertools import cycle
from operator import mul

remainders = [1, 10, 9, 12, 3, 4]


def thirt(n):
    while True:
        new_n = sum(mul(*x) for x in zip(cycle(remainders), (int(d) for d in str(n)[::-1])))
        if new_n == n:
            break
        n = new_n
    return new_n