# https://www.codewars.com/kata/594b8e182fa0a0d7fc000875
def find_E(s):
    if not s:
        return s
    else:
        c = s.lower().count('e')
        return str(c) if c else 'There is no "e".'