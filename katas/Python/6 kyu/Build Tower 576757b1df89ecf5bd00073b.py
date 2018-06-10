# https://www.codewars.com/kata/576757b1df89ecf5bd00073b
def tower_builder(n_floors):
    return [' ' * (n_floors - i - 1) + '*' * (2 * i + 1) + ' ' * (n_floors - i - 1) for i in range(n_floors)]