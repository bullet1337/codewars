# https://www.codewars.com/kata/52fba66badcd10859f00097e
import re


def disemvowel(string):
    return re.sub('[euioa]', '', string, flags=re.IGNORECASE)