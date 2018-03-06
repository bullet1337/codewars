# https://www.codewars.com/kata/5a3bedd38f27f246c200005f
import re


def solve(s):
    while True:
        new_s = ''
        last = 0
        for match in re.finditer('\([^()]*\)', s):
            new_s += s[last:match.start(0)]
            temp = s[match.start(0) + 1:match.end(0) - 1]
            if match.start(0) > 0 and s[match.start(0) - 1] == '-':
                temp = temp.replace('-', '*').replace('+', '-').replace('*', '+')
            if len(temp) > 0 and temp[0] in '+-' and len(new_s) > 0 and new_s[-1] in '+-':
                new_s = new_s[:-1]
            new_s += temp

            last = match.end(0)
        new_s += s[last:]
        s = new_s

        if last == 0:
            break
    if s[0] == '+':
        s = s[1:]
    return s