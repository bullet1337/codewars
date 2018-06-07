# https://www.codewars.com/kata/57fd6c4fa5372ead1f0004aa
import re


patterns = [
    'ci|ce|c(?!h)',
    'ph',
    '([a-z])\\1|(?<=[a-z]{3})(?P<E>e+)([^a-z]|$)',
    'th|wr|wh|w',
    'ou|an|ing\\b|\\bsm',
]

dicts = [
    {'ci': 'si', 'ce': 'se', 'c': 'k'},
    {'ph': 'f'},
    None,
    {'th': 'z', 'wr': 'r', 'wh': 'v', 'w': 'v'},
    {'ou': 'u', 'an': 'un', 'ing': 'ink', 'sm': 'schm'}
]


def replacement(m, week):
    if week != 2:
        r = dicts[week][m.group().lower()]
    else:
        if m.group('E'):
            r = m.group()[:m.start('E') - m.start()] + m.group()[m.end('E') - m.start():]
        else:
            r = m.group()[0]

    if m.group()[0].isupper():
        r = r[0].upper() + r[1:]
    return r

def siegfried(week, txt):
    for i in range(week):
        txt = re.sub(patterns[i], lambda m: replacement(m, i), txt, flags=re.I)
    return txt