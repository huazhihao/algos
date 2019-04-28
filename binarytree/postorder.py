class Node(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def postorderTraversal(root):
    output = []
    s = [root]
    while len(s) > 0:
        n = s.pop()
        if n.left:
            s.append(n.left)
            n.left = None
        if n.right:
            s.append(n.right)
            n.right = None
        output.append(n.val)
    return output[::-1]


root = Node(1, None, Node(2, Node(3), None))
assert [3, 2, 1] == postorderTraversal(root)
