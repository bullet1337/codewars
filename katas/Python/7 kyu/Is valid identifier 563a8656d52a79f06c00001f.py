# https://www.codewars.com/kata/563a8656d52a79f06c00001f
import re


def is_valid(idn):
    return bool(re.match('[a-z_$][a-z0-9_$]*$', idn, re.I))
