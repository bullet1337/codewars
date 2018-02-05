# https://www.codewars.com/kata/59bf943cafcda28e31000130
from collections import Counter


fibs = {
    0: 0,
    1: 1,
}
max_fib = 1


def around_fib(n):
    global max_fib
    for i in range(max_fib + 1, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    max_fib = max(max_fib, n)

    str_fib = str(fibs[n])
    ch = max(Counter(str_fib).items(), key=lambda x: (x[1], -ord(x[0])))
    return 'Last chunk {0}; Max is {2} for digit {1}'.format(str_fib[-(len(str_fib) % 25 or 25):], *ch)