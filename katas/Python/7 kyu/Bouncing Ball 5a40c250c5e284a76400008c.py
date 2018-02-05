# https://www.codewars.com/kata/5a40c250c5e284a76400008c
import math


def bouncing_ball(initial, proportion):
    return math.ceil(round(-math.log(initial, proportion), 10)) 