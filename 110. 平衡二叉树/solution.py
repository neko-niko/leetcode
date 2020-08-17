# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def deep(root: TreeNode) -> int:
            if not root:
                return 0

            left = deep(root.left)
            right = deep(root.right)
            if left < 0 or right < 0:
                return -1

            if abs(left - right) <= 1:
                return 1 + max(left, right)

            return -1

        return deep(root) > 0