# https://www.codewars.com/kata/51c8e37cee245da6b40000bd
def process(line, markers):
    indices = [line.find(m) for m in markers]
    indices = [i for i in indices if i != -1]
    
    if not indices:
        return line
    else:
        return line[:min(indices)].strip()



def solution(string, markers):
    return '\n'.join(process(line, markers) for line in string.split('\n'))