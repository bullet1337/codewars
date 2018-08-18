# https://www.codewars.com/kata/588534713472944a9e000029
class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(node):
    def is_bst_asc(node, min=None, max=None):
        return node is None or (min is None or node.value > min) and (max is None or node.value < max) \
            and is_bst_asc(node.left, min, node.value) and is_bst_asc(node.right, node.value, max)
    
    def is_bst_desc(node, min=None, max=None):
        return node is None or (min is None or node.value > min) and (max is None or node.value < max) \
            and is_bst_desc(node.left, node.value, max) and is_bst_desc(node.right, min, node.value)
    
    return is_bst_asc(node) or is_bst_desc(node)