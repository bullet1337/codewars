# https://www.codewars.com/kata/556deca17c58da83c00002db
def tribonacci(signature, n):
    for _ in range(n - 3):
        signature.append(signature[-3] + signature[-2] + signature[-1])
        
    return signature[:n]