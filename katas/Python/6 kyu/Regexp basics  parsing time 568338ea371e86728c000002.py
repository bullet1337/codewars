# https://www.codewars.com/kata/568338ea371e86728c000002
import re


def to_seconds(time):
    m = re.match(r'(\d{2}):([0-5]\d):([0-5]\d)$(?!.)', time, re.S)
    if m is None:
        return m
    else:
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))