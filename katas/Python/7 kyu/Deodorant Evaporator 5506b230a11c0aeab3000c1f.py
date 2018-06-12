# https://www.codewars.com/kata/5506b230a11c0aeab3000c1f
from itertools import repeat, takewhile, accumulate


def evaporator(content, evap_per_day, threshold):
	return len(list(takewhile(lambda x: x > content * threshold / 100, accumulate(repeat(content), lambda x, y: x * (1 - evap_per_day / 100)))))