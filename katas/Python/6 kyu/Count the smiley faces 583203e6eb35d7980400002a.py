# https://www.codewars.com/kata/583203e6eb35d7980400002a
import re


def count_smileys(arr):
    return len([s for s in arr if re.fullmatch('[:;][-~]?[)D]', s)])