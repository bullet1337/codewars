# https://www.codewars.com/kata/57f8ff867a28db569e000c4a
import re


def kebabize(string):
    def helper(m):
        if m.group().isdigit():
            return ''
        elif m.start() == 0 or string[:m.start()].isdigit():
            return m.group().lower()
        else:
            return '-' + m.group().lower()
        

    return re.sub('[A-Z\d]', helper, string)