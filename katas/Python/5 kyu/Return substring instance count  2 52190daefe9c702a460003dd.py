# https://www.codewars.com/kata/52190daefe9c702a460003dd
import re


def search_substr(full_text, search_text, allow_overlap=True):
    if not search_text:
        return 0

    if not allow_overlap or len(search_text) == 1:
        return len(re.findall(search_text, full_text))
    else:
        return len(re.findall('{}(?={})'.format(search_text[0], search_text[1:]), full_text))