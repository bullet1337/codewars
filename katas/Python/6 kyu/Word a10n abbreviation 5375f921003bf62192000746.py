# https://www.codewars.com/kata/5375f921003bf62192000746
import re


def abbreviate(s):
    return re.sub('[a-z]{4,}', lambda m: m.group()[0] + str(len(m.group()) - 2) + m.group()[-1], s, flags=re.I)