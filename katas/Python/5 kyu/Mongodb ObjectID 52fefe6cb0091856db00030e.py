# https://www.codewars.com/kata/52fefe6cb0091856db00030e
import re
from datetime import datetime


class Mongo(object):
    pattern = '[\da-z]{24}'

    @classmethod
    def is_valid(cls, s):
        return isinstance(s, str) and bool(re.fullmatch(cls.pattern, s))
    
    @classmethod
    def get_timestamp(cls, s):
        return cls.is_valid(s) and datetime.fromtimestamp(int(s[:8], 16))