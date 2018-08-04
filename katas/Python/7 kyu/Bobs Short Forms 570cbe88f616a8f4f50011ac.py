# https://www.codewars.com/kata/570cbe88f616a8f4f50011ac
import re


def short_form(s):
    return re.sub(r'(?!\b)[aioue](?!\b)', '', s, flags=re.I)