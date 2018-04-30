# https://www.codewars.com/kata/525c65e51bf619685c000059
def cakes(recipe, available):
    return min(available.get(ingredient, 0) / count for ingredient, count in recipe.items())