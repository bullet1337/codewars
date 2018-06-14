# https://www.codewars.com/kata/55c4eb777e07c13528000021
from collections import Counter
from math import sqrt, log
from itertools import accumulate, repeat
from operator import mul


def get_primes(number):
    primes = Counter()
    for i in range(2, int(sqrt(number)) + 1):
        while True:
            div, mod = divmod(number, i)
            if mod == 0:
                number = div
                primes[i] += 1
            else:
                break
    if number != 1:
        primes[number] += 1

    return primes


def zeroes(base, number):
    return min(sum(map(lambda x: number // x, accumulate(repeat(prime, int(log(number, prime))), mul))) // count for prime, count in get_primes(base).items())