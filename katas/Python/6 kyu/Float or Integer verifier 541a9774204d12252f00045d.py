# https://www.codewars.com/kata/541a9774204d12252f00045d
import re


def i_or_f(arr):
    return bool(re.fullmatch('[+-]?\d*(\.\d*)?(e[+-]?\d+)?', arr, re.I))