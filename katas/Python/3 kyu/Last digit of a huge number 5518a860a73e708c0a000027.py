# https://www.codewars.com/kata/5518a860a73e708c0a000027
from functools import reduce


def last_two_digits_mul(x, y):
    x2, x1 = divmod(x % 100, 10)
    y2, y1 = divmod(y % 100, 10)
    return (((y1 * x2 + y1 * x1 // 10) % 10 + y2 * x1 % 10) % 10) * 10 + y1 * x1 % 10


def last_two_digits_pow(x, y):
    if y == 0:
        return 1
    elif y == 1:
        if x < 10:
            return x

        x %= 100
        if x < 10:
            return x + 100
        else:
            return x

    if x == 0:
        return 0
    elif x == 1:
        return 1

    x %= 100
    x2, x1 = divmod(x, 10)
    if x1 == 0:
        return 100
    elif x1 == 1:
        x2 = x2 * (y % 10) % 10
        if x2 == 0:
            return 101
        else:
            return x2 * 10 + 1
    elif x1 == 5:
        if x2 % 2 == 0:
            if x == 5 and y == 1:
                return 5
            else:
                return 25
        else:
            return [25, 75][y % 2]
    elif x1 == 9:
        div, mod = divmod(y, 2)
        x_square = last_two_digits_mul(x, x)
        last_two = last_two_digits_pow(x_square, div)

        if mod != 0:
            last_two = last_two_digits_mul(last_two, x)

        return last_two
    elif x1 == 3 or x1 == 7:
        div, mod = divmod(y, 4)
        x_square = last_two_digits_mul(x, x)
        x_forth = last_two_digits_mul(x_square, x_square)
        last_two = last_two_digits_pow(x_forth, div)

        if mod != 0:
            x_rest = x
            for i in range(mod - 1):
                x_rest = last_two_digits_mul(x_rest, x)

            last_two = last_two_digits_mul(last_two, x_rest)

        return last_two
    elif x1 == 2 or x1 == 4 or x1 == 6 or x1 == 8:
        x_half = x // 2
        x_half_last_two = last_two_digits_pow(x_half, y)

        y2, y1 = divmod(y, 10)
        two_last_two = 1
        if y2 != 0:
            two_last_two = [76, 24][y2 % 2]

        if y1 != 0:
            two_last_two = last_two_digits_mul(two_last_two, pow(2, y1))

        return last_two_digits_mul(x_half_last_two, two_last_two)
        

def last_digit(lst):
    return reduce(lambda x, y: last_two_digits_pow(y, x), reversed(lst), 1) % 10