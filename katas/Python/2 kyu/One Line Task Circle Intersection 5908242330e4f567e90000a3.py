# https://www.codewars.com/kata/5908242330e4f567e90000a3
from math import*;circleIntersection=lambda a,b,r:(lambda q:int(r*r*(q-sin(q))))(2*acos(min(1,hypot(a[0]-b[0],a[1]-b[1])/2/r)))