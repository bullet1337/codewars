# https://www.codewars.com/kata/52761ee4cffbc69732000738
good_worth = [1, 2, 3, 3, 4, 10]
evil_worth = [1, 2, 2, 2, 3, 5, 10]
answers = [
    'Battle Result: No victor on this battle field',
    'Battle Result: Good triumphs over Evil',
    'Battle Result: Evil eradicates all trace of Good'
]


def goodVsEvil(good, evil):
    def sign(x):
        return 1 if x > 0 else -1 if x < 0 else 0

    return answers[sign(sum(w * c for w, c in zip(good_worth, map(int, good.split()))) - sum(w * c for w, c in zip(evil_worth, map(int, evil.split()))))]