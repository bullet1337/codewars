# https://www.codewars.com/kata/548db0bd1df5bbf29b0000b7
import re

valid_date = re.compile('\[(02-(0[1-9]|1\d|2[1-8])|(0[13-9]|1[12])-(3(0|(?<=(0[13578]|10|12)-3)1)|0[1-9]|[12]\d))\]')