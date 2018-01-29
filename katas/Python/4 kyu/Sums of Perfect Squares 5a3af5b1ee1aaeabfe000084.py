# https://www.codewars.com/kata/5a3af5b1ee1aaeabfe000084
from math import sqrt


def sum_of_squares(n):
    n_sqrt = int(sqrt(n))

    if n == n_sqrt * n_sqrt:
        return 1

    div, mod = divmod(n, 4)
    while mod == 0:
        div, mod = divmod(div, 4)
    if (div * 4 + mod) % 8 == 7:
        return 4

    for i in range(1, n_sqrt + 1):
        temp = n - i * i
        temp_sqrt = int(sqrt(temp))
        if temp == temp_sqrt * temp_sqrt:
            return 2

    return 3