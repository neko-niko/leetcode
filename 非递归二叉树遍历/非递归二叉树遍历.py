
class TreeNode(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def Traversing(root: TreeNode):
    stack = []

    stack.append(root)
    while stack:
        cur = stack[-1]
        if cur.left is not None:
            stack.append(cur.left)
            cur.left = None
            continue
        if cur.right is not None:
            stack.append(cur.right)
            cur.right = None
            continue
        print(cur.value)
        stack.pop()
