# https://www.codewars.com/kata/556e0fccc392c527f20000c5
def Xbonacci(signature, n):
    x = len(signature)
    for _ in range(n - x):
        signature.append(sum(signature[-x:]))
        
    return signature[:n]