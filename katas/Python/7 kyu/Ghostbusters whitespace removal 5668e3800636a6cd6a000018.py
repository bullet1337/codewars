# https://www.codewars.com/kata/5668e3800636a6cd6a000018
def ghostbusters(building):
    res = building.replace(' ', '')
    return res if len(res) != len(building) else 'You just wanted my autograph didn\'t you?'
    