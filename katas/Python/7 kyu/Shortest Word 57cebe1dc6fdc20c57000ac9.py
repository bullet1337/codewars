# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
def find_short(s):
    return min(len(w) for w in s.split())