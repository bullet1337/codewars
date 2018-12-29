# https://www.codewars.com/kata/5aaae0f5fd8c069e8c00016e
def compound_match(words, target):
    index = {}
    for i, w in enumerate(words):
        if w not in index:
            index[w] = i
    pairs = [(target[:i], target[i:]) for i in range(1, len(target))]
    
    for pre, suf in pairs:
        if pre in index and suf in index:
            indices = [index[pre], index[suf]]
            return [pre, suf, indices] if indices[0] < indices[1] else [suf, pre, indices]
    return None