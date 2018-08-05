# https://www.codewars.com/kata/592421cb7312c23a990000cf
import  re


def repl(m):
    return str(len(m.group())) + m.group(2)


def look_and_say_sequence(first_element, n):
    for _ in range(n - 1):
        first_element = re.sub(r'((.)\2*)', repl, first_element)
    return first_element