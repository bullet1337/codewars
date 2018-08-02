# https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023
import re


def validate_usr(username):
    return re.fullmatch('[a-z0-9_]{4,16}', username) is not None