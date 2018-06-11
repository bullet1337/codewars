# https://www.codewars.com/kata/54df2067ecaa226eca000229
def f(n):
    return n * (n + 1) / 2 if isinstance(n, int) and n > 0 else None