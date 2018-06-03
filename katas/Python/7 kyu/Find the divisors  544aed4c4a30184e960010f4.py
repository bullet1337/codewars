# https://www.codewars.com/kata/544aed4c4a30184e960010f4
from math import sqrt


def divisors(integer):
    dvsrs = [i for i in range(2, integer) if integer % i == 0]
    return dvsrs or '{} is prime'.format(integer)