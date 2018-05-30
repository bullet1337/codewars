# https://www.codewars.com/kata/52c4dd683bfd3b434c000292
import re


def is_interesting(number, awesome_phrases):
    def helper(number):
        if number < 100:
            return 0
            
        str_num = str(number)
        if re.fullmatch('[1-9]0+|(\d)\1+', str_num) or number in awesome_phrases:
            return 2
        
        order = None
        for i in range(len(str_num) - 1):
            if ord(str_num[i]) + 1 == ord(str_num[i + 1]) or str_num[i] == '9' and str_num[i + 1] == '0':
                if order is None:
                    order = True
                elif not order:
                    break
                if str_num[i + 1] == '0' and i + 1 != len(str_num) - 1:
                    break
            elif ord(str_num[i]) - 1 == ord(str_num[i + 1]):
                if order is None:
                    order = False
                elif order:
                    break
                if str_num[i + 1] == '0' and i + 1 != len(str_num) - 1:
                    break
            else:
                break
        else:
            return 2
            
        if str_num == str_num[::-1]:
            return 2
        
        return 0
        
    return helper(number) or (1 if helper(number + 1) or helper(number + 2) else 0)