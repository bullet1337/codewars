# https://www.codewars.com/kata/529adbf7533b761c560004e5
memo = {0: 0, 1: 1}


def fibonacci(n):
    k = memo.get(n, None)
    if k is None:
        k = fibonacci(n - 1) + fibonacci(n - 2)
        memo[n] = k
    return k