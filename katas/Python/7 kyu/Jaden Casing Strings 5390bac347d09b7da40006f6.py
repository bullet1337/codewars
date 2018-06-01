# https://www.codewars.com/kata/5390bac347d09b7da40006f6
import re


def toJadenCase(string):
    return re.sub('\\b(?<!\')(\w)', lambda m: m.group(1).upper(), string)