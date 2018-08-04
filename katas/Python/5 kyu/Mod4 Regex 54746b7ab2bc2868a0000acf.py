# https://www.codewars.com/kata/54746b7ab2bc2868a0000acf
import re

class Mod:
    mod4 = re.compile('.*?\[[+-]?([048]|\d*?([02468][048]|[13579][26]))\]')