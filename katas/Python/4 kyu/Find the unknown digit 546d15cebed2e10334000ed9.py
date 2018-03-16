# https://www.codewars.com/kata/546d15cebed2e10334000ed9
import re


def solve_runes(runes):
    index = runes.find('=')
    groups = (runes[:index], runes[index + 1:])
    mark = re.findall('(^|[-=+*])\?[\d?]', runes, re.MULTILINE)
    for d in ('0' if not mark else '') + '123456789':
        if d in runes:
            continue

        if eval(groups[0].replace('?', d)) == int(groups[1].replace('?', d)):
            return int(d)

    return -1