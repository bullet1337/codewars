# https://www.codewars.com/kata/52b757663a95b11b3d00062d
def to_weird_case(string):
    return ' '.join(''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)) for word in string.split())