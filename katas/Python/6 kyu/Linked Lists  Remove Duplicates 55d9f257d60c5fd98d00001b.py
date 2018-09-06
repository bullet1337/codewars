# https://www.codewars.com/kata/55d9f257d60c5fd98d00001b
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    data_set = set()
    prev = None
    node = head
    while node is not None:
        if node.data in data_set:
            prev.next = node.next
        else:
            data_set.add(node.data)
            prev = node
        node = node.next
    return head