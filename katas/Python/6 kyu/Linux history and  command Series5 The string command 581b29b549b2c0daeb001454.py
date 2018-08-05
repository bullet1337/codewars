# https://www.codewars.com/kata/581b29b549b2c0daeb001454
import re


def bang_contain_string(s, history): 
    m = re.findall(r'\s+\d+\s+((?=\w).*{}.*)'.format(re.escape(s)), history)
    return '!{}: event not found'.format(s) if not m else m[-1]