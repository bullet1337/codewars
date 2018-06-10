# https://www.codewars.com/kata/539ee3b6757843632d00026b
def capitals(word):
    return [i for i, l in enumerate(word) if l.isupper()]