# https://www.codewars.com/kata/58708934a44cfccca60000c4
import re


replacement_map = {
    'F': '<span style="color: pink">{}</span>',
    'L': '<span style="color: red">{}</span>',
    'R': '<span style="color: green">{}</span>',
}


def replacement(match):
    return replacement_map.get(match.group(1)[0], '<span style="color: orange">{}</span>').format(match.group(1))


def highlight(code):
    return re.sub('(F+|L+|R+|\d+)', replacement, code)