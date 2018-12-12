# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b
def is_uppercase(inp):
    return all(l.isupper() for l in inp if l.isalpha())