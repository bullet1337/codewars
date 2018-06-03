# https://www.codewars.com/kata/54b8204dcd7f514bf2000348
import re


class Simplexer(object):

    def __init__(self, expression):
        pattern = '(?P<operator>[+\-*\/%\(\)=])|(?P<boolean>true|false)|(?P<integer>\d+)|(?P<string>".*?")|(?P<keyword>if|else|for|while|return|func|break)|(?P<whitespace>\s+)|(?P<identifier>[a-zA-Z$_][\w$]*)'
        self.tokens = (Token(m.group(m.lastgroup), m.lastgroup) for m in re.finditer(pattern, expression))
    
    def __iter__(self):
        return self.tokens
                
    def __next__(self):
        return next(self.tokens)