# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
import string


def is_pangram(s):
    return not(set(string.ascii_lowercase) - set(s.lower()))