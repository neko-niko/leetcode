class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.cot = 0
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot:
            node = self.KthNode(pRoot.left, k)
            if node:
                return node

            self.cot += 1
            if self.cot == k:
                return pRoot
            node = self.KthNode(pRoot.right, k)
            if node:
                return node




