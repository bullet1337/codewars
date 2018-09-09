# https://www.codewars.com/kata/55e725b930957a038a000042
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def reverse(head, prev=None):
    if head is None:
        return prev
    else:
        return reverse(head.next, Node(head.data, prev))