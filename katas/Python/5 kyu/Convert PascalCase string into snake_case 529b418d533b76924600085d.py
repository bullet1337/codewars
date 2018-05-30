# https://www.codewars.com/kata/529b418d533b76924600085d
import re


def replacement(match):
  return ('_' if match.start(1) > 0 else '') + match.group(1).lower()


def to_underscore(string):
    if isinstance(string, int):
        return str(string)
    else:
        return re.sub('([A-Z])', replacement, string)