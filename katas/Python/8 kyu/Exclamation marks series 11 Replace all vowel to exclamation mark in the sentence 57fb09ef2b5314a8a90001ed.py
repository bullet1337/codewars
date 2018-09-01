# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed
import re


def replace_exclamation(s):
    return re.sub(r'[aioue]', '!', s, flags=re.I)