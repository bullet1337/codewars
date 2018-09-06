# https://www.codewars.com/kata/55d17ddd6d7868493e000074
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def append(listA, listB):
    if listA is None:
        return listB
    elif listB is None:
        return listA
    
    node = listA
    while node.next is not None:
        node = node.next
    node.next = listB
    return listA