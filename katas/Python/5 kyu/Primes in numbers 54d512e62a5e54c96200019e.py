# https://www.codewars.com/kata/54d512e62a5e54c96200019e
from collections import Counter


def primeFactors(n):
    primes = Counter()
    d = 2
    while d * d <= n:
        if n % d == 0:
            primes[d] += 1
            n //= d
        else:
            d += 1
    if n != 1:
        primes[n] += 1
    return ''.join('({}{})'.format(prime, '**%d' % pow if pow > 1 else '') for prime, pow in sorted(primes.items()))