# https://www.codewars.com/kata/55e5253dcd20f821c400008e
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def shuffle_merge(first, second):
    if first is None or second is None:
        return first or second
    
    head = current = first
    first = first.next
    first, second = second, first
    while first is not None and second is not None:
        current.next = first
        current = current.next
        first = first.next
        first, second = second, first     
    current.next = first or second
    return head