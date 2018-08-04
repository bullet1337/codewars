# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
import re


numbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}

tens = {
    'thousand': 1000,
    'million': 1000000
}


def parse_triplet(triplet):
    result = 0
    for str_number in triplet.split():
        if str_number == 'hundred':
            result *= 100
        else:
            number = numbers.get(str_number)
            if str_number == 'and':
                continue
                
            if number is None:
                digits = str_number.split('-')
                result += (numbers[digits[0]] + numbers[digits[1]])
            else:
                result += number
    return result


def parse_int(string):        
    result = temp = 0
    for i, triplet in enumerate(re.split(' ?(thousand|million) ?', string)):
        if triplet not in tens:
            temp = parse_triplet(triplet)
        else:
            result += temp * tens[triplet]
    return result + temp