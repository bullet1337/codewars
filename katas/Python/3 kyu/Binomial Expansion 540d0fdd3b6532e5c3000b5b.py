# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b
from functools import lru_cache
import re


@lru_cache(maxsize=None)
def fact(n):
    return 1 if n < 1 else n * fact(n - 1)


def c(n, k):
    return fact(n) // (fact(k) * fact(n - k))


def format(a, x=True):
    return ('+' if a > 0 else '-') + ('' if x and abs(a) == 1 else str(abs(a)))
        

def format_x(x, pow):
    return '' if pow == 0 else (x  + ('' if pow == 1 else '^' + str(pow)))


def expand(expr):    
    m = re.match(r'\(([+-]?\d*)([a-z])([+-]?\d+)?\)\^(\d+)', expr)
    a, x, b, n = m.groups()
    a = (int(a) if a != '-' else -1) if a else 1
    b = int(b) if b else 0
    n = int(n)
    
    res = None
    if n == 0:
        res = '1'
    elif n == 1:
        res = format(a) + x + format(b, x=False)
    elif b == 0:
        res = format(pow(a, n)) + var
    else:
        res = ''.join(format(c(n, k) * pow(a, n - k) * pow(b, k), x=n!=k) + format_x(x, n - k) for k in range(n + 1))
    return res[res[0] == '+':] 