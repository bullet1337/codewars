# https://www.codewars.com/kata/55d0c7ee7c0d30a12b000045
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sorted_insert(head, data):
    prev = None
    node = head
    while node is not None and node.data < data:
        prev = node
        node = node.next
        
    if prev is None:
        return Node(data, head)
    else:
        prev.next = Node(data, prev.next)
        return head


def insert_sort(head):
    head_sorted = None
    while head is not None:
        head_sorted = sorted_insert(head_sorted, head.data)
        head = head.next
    return head_sorted