# https://www.codewars.com/kata/56541980fa08ab47a0000040
def printer_error(s):
    return '{}/{}'.format(sum(1 for c in s if c > 'm'), len(s))