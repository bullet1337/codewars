# https://www.codewars.com/kata/5682e1082cc7862db5000039
import re


def to_integer(string):
    x = re.match(r'[+-]?(?:(?P<i2>0b[01]+)|(?P<i8>0o[0-7]+)|(?P<i16>0x[0-9a-fA-F]+)|(?P<i10>\d+))$(?!.)', string, re.S)
    return int(string, int(x.lastgroup[1:])) if x else None