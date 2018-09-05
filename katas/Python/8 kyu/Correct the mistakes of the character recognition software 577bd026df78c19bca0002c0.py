# https://www.codewars.com/kata/577bd026df78c19bca0002c0
import re

mistakes = {
    '5': 'S',
    '0': 'O',
    '1': 'I'
}


def correct(string):
    return re.sub('[501]', lambda m: mistakes[m.group()], string)