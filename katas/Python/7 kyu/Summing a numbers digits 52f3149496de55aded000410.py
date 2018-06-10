# https://www.codewars.com/kata/52f3149496de55aded000410
def sumDigits(number):
    return sum(map(int, str(abs(number))))