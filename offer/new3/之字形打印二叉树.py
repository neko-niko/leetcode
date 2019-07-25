class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.stack = [[], []]
        self.label = 0
    def Print(self, pRoot):
        result = []
        curr = 0
        self.stack[0].append(pRoot)
        while self.stack[0] or self.stack[1]:
            result.append([])
            while self.stack[self.label]:
                if self.label == 0:
                    node = self.stack[self.label].pop()
                    result[curr].append(node.val)
                    if node.left is not None:
                        self.stack[1-self.label].append(node.left)
                    if node.right is not None:
                        self.stack[1-self.label].append(node.right)
                else:
                    node = self.stack[self.label].pop()
                    result[curr].append(node.val)
                    if node.right is not None:
                        self.stack[1-self.label].append(node.right)
                    if node.left is not None:
                        self.stack[1-self.label].append(node.left)
            curr += 1
            self.label = 1 - self.label
        return result