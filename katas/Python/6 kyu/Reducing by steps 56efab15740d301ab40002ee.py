# https://www.codewars.com/kata/56efab15740d301ab40002ee
from itertools import accumulate
from math import gcd
from operator import add


def lcm(a, b):
    return a * b // gcd(a, b)


def gcdi(a):
    return accumulate(a, lambda a, b: gcd(abs(a), abs(b)))
    
    
def lcmu(a):
    return accumulate(a, lambda a, b: lcm(abs(a), abs(b)))
    
    
def som(a):
    return accumulate(a, add)
  
  
def maxi(a):
    return accumulate(a, max)
    
    
def mini(a):
    return accumulate(a, min)
    
    
def oper_array(fct, arr, init):
    return list(fct([init] + arr))[1:]