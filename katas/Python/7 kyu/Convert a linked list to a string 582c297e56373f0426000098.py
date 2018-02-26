# https://www.codewars.com/kata/582c297e56373f0426000098
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def iter_linked_list(current):
    while current is not None:
        yield current.data
        current = current.next
    yield None


def stringify(list):
    return ' -> '.join(str(x) for x in iter_linked_list(list))