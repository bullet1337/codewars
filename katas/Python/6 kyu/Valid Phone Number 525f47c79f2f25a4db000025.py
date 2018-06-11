# https://www.codewars.com/kata/525f47c79f2f25a4db000025
import re


def validPhoneNumber(x):
    return bool(re.fullmatch('\(\d{3}\) \d{3}-\d{4}', x))