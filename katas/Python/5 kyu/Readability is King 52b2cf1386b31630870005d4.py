# https://www.codewars.com/kata/52b2cf1386b31630870005d4
import re


def syllables(word):
    return len(re.findall('[aioue]{1,2}', word, flags=re.I))

def flesch_kincaid(text):
    sentences = [re.split('\s', s.strip()) for s in re.split('[.!?]', text) if s]
    total_words = sum(len(s) for s in sentences)
    return round(0.39 * total_words / len(sentences) + 11.8 * sum(syllables(w) for s in sentences for w in s) / total_words - 15.59, 2)
    