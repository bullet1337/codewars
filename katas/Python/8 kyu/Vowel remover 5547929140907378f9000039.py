# https://www.codewars.com/kata/5547929140907378f9000039
import re


def shortcut(s):
    return re.sub('[euioa]', '', s)