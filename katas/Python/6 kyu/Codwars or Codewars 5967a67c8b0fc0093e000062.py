# https://www.codewars.com/kata/5967a67c8b0fc0093e000062
import re


def find_codwars(url):
    return bool(re.match(r'(https?:\/\/)?([a-z]+\.)*codwars\.com([\/?]|\Z)', url))