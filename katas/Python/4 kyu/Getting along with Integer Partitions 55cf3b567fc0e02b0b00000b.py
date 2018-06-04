# https://www.codewars.com/kata/55cf3b567fc0e02b0b00000b
from functools import reduce
from operator import mul


def part(n):
    def combos(n, m = 1):
        if n < m:
            return []
        res = [[n]]
        for i in xrange(m, n):
            l = [i]
            for j in combos(n - i, i):
               res += [l + j]
        return res

    x = sorted(set(reduce(mul, x) for x in combos(n)))
    return 'Range: {} Average: {:0.2f} Median: {:0.2f}'.format(x[-1] - x[0], sum(x) * 1.0 / len(x), x[len(x) // 2] if len(x) % 2 else (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2.0)