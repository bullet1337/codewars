# https://www.codewars.com/kata/526dbd6c8c0eb53254000110
import re


def alphanumeric(string):
    return re.fullmatch('[a-z\d]+', string, flags=re.I) is not None