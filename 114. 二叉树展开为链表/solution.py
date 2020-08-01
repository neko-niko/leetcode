# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:

        def deep(root: TreeNode):
            if not root:
                return

            deep(root.left)
            deep(root.right)
            right_node = root.right
            left_node = root.left
            root.left = None
            if not left_node:
                return

            root.right = left_node

            while left_node.right:
                left_node = left_node.right
            left_node.right = right_node

        deep(root)
