# https://www.codewars.com/kata/55d410c492e6ed767000004f
import re


def repl(match):
    return str(match.start() + 1)


def vowel_2_index(string):
    return re.sub('[aeiou]', repl, string, flags=re.I)