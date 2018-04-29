# https://www.codewars.com/kata/523a86aa4230ebb5420001e1
from collections import Counter   


def anagrams(word, words):
    word_counter = Counter(word)
    return [w for w in words if Counter(w) == word_counter]