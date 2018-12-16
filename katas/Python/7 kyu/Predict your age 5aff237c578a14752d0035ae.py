# https://www.codewars.com/kata/5aff237c578a14752d0035ae
from math import sqrt


def predict_age(*ages):
    return sqrt(sum(age * age for age in ages)) // 2