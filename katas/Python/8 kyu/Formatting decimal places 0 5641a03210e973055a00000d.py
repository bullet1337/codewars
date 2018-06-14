# https://www.codewars.com/kata/5641a03210e973055a00000d
def two_decimal_places(n):
    return round(round(n, 2) + 0.01 * (n * 1000 % 10 == 5), 2)