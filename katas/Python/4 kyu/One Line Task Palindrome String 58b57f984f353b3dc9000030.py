# https://www.codewars.com/kata/58b57f984f353b3dc9000030
palindrome=lambda n,c:c+c[-1]*(n-2*len(c)+1)+c[-2::-1]