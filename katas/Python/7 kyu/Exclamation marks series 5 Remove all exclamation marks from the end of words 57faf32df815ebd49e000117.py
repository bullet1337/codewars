# https://www.codewars.com/kata/57faf32df815ebd49e000117
def remove(s):
    return ' '.join(w.rstrip('!') or w for w in s.split())