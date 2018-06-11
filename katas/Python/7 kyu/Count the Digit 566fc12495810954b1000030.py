# https://www.codewars.com/kata/566fc12495810954b1000030
def nb_dig(n, d):
    return sum(str(i ** 2).count(str(d)) for i in range(n + 1))