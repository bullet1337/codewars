# https://www.codewars.com/kata/53f40dff5f9d31b813000774
def recoverSecret(triplets):
    word = ''
    while triplets:
        letter_pos = {}
        for triplet in triplets:
            for i, letter in enumerate(triplet):
                letter_pos[letter] = max(letter_pos.get(letter, 0), i)

        letter = next(l for l, pos in letter_pos.items() if pos == 0)
        word += letter
        triplets = [[l for l in triplet if l != letter] for triplet in triplets]
        triplets = [triplet for triplet in triplets if triplet]
    return word