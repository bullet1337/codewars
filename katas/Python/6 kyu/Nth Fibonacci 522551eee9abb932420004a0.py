# https://www.codewars.com/kata/522551eee9abb932420004a0
def nth_fib(n):
    return n - 1 if n < 3 else nth_fib(n - 2) + nth_fib(n - 1)
