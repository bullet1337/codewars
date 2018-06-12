# https://www.codewars.com/kata/587731fda577b3d1b0001196
import re


def camel_case(string):
    return re.sub('\\b[a-z]', lambda m: m.group().upper(), string, flags=re.I).replace(' ', '')