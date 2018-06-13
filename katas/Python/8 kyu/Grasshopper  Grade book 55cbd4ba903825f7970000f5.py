# https://www.codewars.com/kata/55cbd4ba903825f7970000f5
def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score <= 100: return 'A'
    elif 80 <= score < 90: return 'B'
    elif 70 <= score < 80: return 'C'
    elif 60 <= score < 70: return 'D'
    else: return 'F'    