# https://www.codewars.com/kata/5b37a50642b27ebf2e000010
import re


def sum_of_a_beach(beach):
    return len(re.findall('sun|sand|water|fish', beach, re.I))