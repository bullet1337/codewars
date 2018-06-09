# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
def openOrSenior(data):
    return ['Senior' if e[0] >= 55 and e[1] > 7 else 'Open' for e in data]