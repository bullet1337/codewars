# https://www.codewars.com/kata/54c2fc0552791928c9000517
def f(n, m):
    return n // m * (m * (m - 1) / 2) + n % m * (n % m + 1) / 2