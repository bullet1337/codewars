# https://www.codewars.com/kata/56efc695740d30f963000557
def to_alternating_case(string):
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)