# https://www.codewars.com/kata/525f039017c7cd0e1a000a26
def palindrome_chain_length(n, steps=0):
    s = str(n)
    if s == s[::-1]:
        return steps
    else:
        return palindrome_chain_length(n + int(s[::-1]), steps + 1)