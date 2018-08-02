# https://www.codewars.com/kata/5389864ec72ce03383000484
import re


def autocomplete(i, d):
    i = re.sub('[^a-z]', '', i, flags=re.I).lower()
    return [w for w in d if re.sub('[^a-z]', '', w, flags=re.I).lower().startswith(i)][:5]