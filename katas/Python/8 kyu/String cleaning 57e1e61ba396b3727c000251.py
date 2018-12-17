# https://www.codewars.com/kata/57e1e61ba396b3727c000251
import re


def string_clean(s):
    return re.sub('\d', '', s)