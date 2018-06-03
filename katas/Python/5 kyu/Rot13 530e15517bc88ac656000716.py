# https://www.codewars.com/kata/530e15517bc88ac656000716
import string

char_map = {chr(ord('a') + i): chr(ord('a') + (i + 13) % 26) for i in range(26)}
char_map.update({f.upper(): t.upper() for f, t in char_map.items()})


def rot13(message):
    return ''.join(char_map.get(c, c) for c in message)