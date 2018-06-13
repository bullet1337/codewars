# https://www.codewars.com/kata/57fae964d80daa229d000126
def remove(s):
    return s[:len(s) - (s[-1] == '!')] if s else s