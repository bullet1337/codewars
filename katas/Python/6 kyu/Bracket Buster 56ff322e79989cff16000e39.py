# https://www.codewars.com/kata/56ff322e79989cff16000e39
import re


def bracket_buster(string):
    return re.findall(r'\[(.*?)\]', string) if isinstance(string, str) else 'Take a seat on the bench.'