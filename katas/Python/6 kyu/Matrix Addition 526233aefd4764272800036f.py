# https://www.codewars.com/kata/526233aefd4764272800036f
def matrix_addition(a, b):
    return [[a_ij + b_ij for a_ij, b_ij in zip(a_i, b_i)] for a_i, b_i in zip(a, b)]