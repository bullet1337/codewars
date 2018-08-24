# https://www.codewars.com/kata/5680781b6b7c2be860000036
def vowel_indices(word):
    return [i + 1 for i, l in enumerate(word) if l.lower() in 'eyuioa']