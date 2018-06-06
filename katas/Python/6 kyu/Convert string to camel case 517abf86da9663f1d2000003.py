# https://www.codewars.com/kata/517abf86da9663f1d2000003
import re


def to_camel_case(text):
    return re.sub('[-_][a-z]', lambda m: m.group()[1:].upper(), text, flags=re.I)