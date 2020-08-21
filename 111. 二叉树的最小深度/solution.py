# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def deep(root: TreeNode) -> int:
            if not root:
                return 0

            if not root.left and root.right:
                return 1+deep(root.right)
            if not root.right and root.left:
                return 1+deep(root.left)

            left = deep(root.left)
            right = deep(root.right)
            return 1 + min(left, right)

        return deep(root)
