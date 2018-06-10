# https://www.codewars.com/kata/5202ef17a402dd033c000009
import re


def title_case(title, minor_words=''):
    minor_words = set(map(str.lower, minor_words.split()))
    def repl(m):
        if m.start() == 0 or m.group().lower() not in minor_words:
            return m.group().title()
        else:
            return m.group().lower()
            
    return re.sub('[a-z]+', repl, title, flags=re.I)