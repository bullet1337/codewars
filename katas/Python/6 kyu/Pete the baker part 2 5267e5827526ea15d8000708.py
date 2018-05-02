# https://www.codewars.com/kata/5267e5827526ea15d8000708
from math import ceil


def get_missing_ingredients(recipe, added):
    missing_portion = {i: added.get(i, 0) * 1.0 / c for i, c in recipe.items()}
    cakes_number = max(ceil(portion) for portion in missing_portion.values())
    return {i: round((cakes_number - c) * recipe[i], 1) for i, c in missing_portion.items() if c != cakes_number}
