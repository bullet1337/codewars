# https://www.codewars.com/kata/5411c4205f3a7fd3f90009ea
import re


def string_parse(string):
    return re.sub(r'([a-zA-Z])\1(\1+)', r'\1\1[\2]', string) if isinstance(string, str) else 'Please enter a valid string'