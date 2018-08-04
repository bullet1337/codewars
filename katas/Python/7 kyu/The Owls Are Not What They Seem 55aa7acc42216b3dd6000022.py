# https://www.codewars.com/kata/55aa7acc42216b3dd6000022
import re


def owl_pic(text):
    text = re.sub('[^8WTYUIOAHXVM]', '', text, flags=re.I).upper()
    return text + "''0v0''"+ text[::-1]