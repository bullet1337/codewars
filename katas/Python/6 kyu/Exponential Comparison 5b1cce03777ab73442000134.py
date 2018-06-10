# https://www.codewars.com/kata/5b1cce03777ab73442000134
from math import log


def compare(number1, number2):
    return number1 if number1[1] * log(number1[0], number2[0]) > number2[1] else number2