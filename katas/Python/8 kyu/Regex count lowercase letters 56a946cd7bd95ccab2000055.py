# https://www.codewars.com/kata/56a946cd7bd95ccab2000055
import re


def lowercase_count(strng):
    return re.subn('[a-z]', '', strng)[1]