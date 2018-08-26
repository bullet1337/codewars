# https://www.codewars.com/kata/58223370aef9fc03fd000071
import re


def dashatize(num):
    return re.sub(r'((?!^)[13579]|(?<=[13579])[02468])', r'-\1', str(abs(num))) if num is not None else 'None'