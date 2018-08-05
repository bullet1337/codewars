# https://www.codewars.com/kata/5814bf3f3db1ffc0180000d3
import re


def bang_n(n, history): 
    m = re.search(r'\s+{}\s+(.*)'.format(n), history)
    return '!{}: event not found'.format(n) if m is None else m.group(1)
