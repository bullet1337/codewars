# https://www.codewars.com/kata/58ade2233c9736b01d0000b3
from random import randint


def password_gen():
    return ''.join(chr(randint(ord('a'), ord('z'))) for _ in range(randint(5, 19))).title() + str(randint(0, 9))