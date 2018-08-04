# https://www.codewars.com/kata/5b39e3772ae7545f650000fc
def remove_duplicate_words(s):
    return ' '.join(sorted(set(s.split()), key=lambda x: s.index(x)))