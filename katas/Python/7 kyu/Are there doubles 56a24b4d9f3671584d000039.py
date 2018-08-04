# https://www.codewars.com/kata/56a24b4d9f3671584d000039
import re


def double_check(strng):
    return bool(re.search(r'(.)\1', strng, re.I))