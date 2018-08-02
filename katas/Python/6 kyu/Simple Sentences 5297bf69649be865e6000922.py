# https://www.codewars.com/kata/5297bf69649be865e6000922
import re


def make_sentences(parts):
    return re.sub('\.+', '', re.sub(' ,', ',', ' '.join(parts))).strip() + '.'