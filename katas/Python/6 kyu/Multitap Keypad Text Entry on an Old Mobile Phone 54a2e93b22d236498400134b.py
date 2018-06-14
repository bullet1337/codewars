# https://www.codewars.com/kata/54a2e93b22d236498400134b
keyboard = ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', '*', ' 0', '#']
button_presses = {l: i + 1 for button in keyboard for i, l in enumerate(button)}


def presses(phrase):
    return sum(button_presses[l.upper()] for l in phrase)