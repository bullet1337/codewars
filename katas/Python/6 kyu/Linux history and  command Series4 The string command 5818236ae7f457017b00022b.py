# https://www.codewars.com/kata/5818236ae7f457017b00022b
import re


def bang_start_string(s, history): 
    m = re.findall(r'^\s+\d+\s+({}.*)'.format(re.escape(s)), history, flags=re.M)
    return '!{}: event not found'.format(s) if not m else m[-1]