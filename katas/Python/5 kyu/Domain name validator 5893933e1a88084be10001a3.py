# https://www.codewars.com/kata/5893933e1a88084be10001a3
import re


def validate(domain):
    return len(domain) <= 253 and re.match('^([a-z\d]([a-z\d-]{,61}[a-z\d])?\.){1,126}(?!\d+$)[a-z\d]([a-z\d-]{,61}[a-z\d])?$', domain, re.I)