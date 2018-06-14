# https://www.codewars.com/kata/544483c6435206617a00012c
from collections import Counter
from math import sqrt, log
from itertools import imap, repeat
from operator import mul


def get_primes(number):
    primes = Counter()
    d = 2
    while d * d <= number:
        if number % d == 0:
            primes[d] += 1
            number //= d
        else:
            d += 1
    if number != 1:
        primes[number] += 1
    return primes


def trailing_zeros(number, base):
    if number == 0:
        return 0

    zeros = float('inf')
    for prime, count in get_primes(base).items():
        prime_zeros = 0
        power = prime
        for _ in range(int(log(number, prime))):
            prime_zeros += number // power
            power *= prime
        prime_zeros //= count
        if prime_zeros == 0:
            return 0
        else:
            zeros = min(zeros, prime_zeros)
    return zeros
