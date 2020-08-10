from functools import lru_cache

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        @lru_cache(1 << 13)
        def deep(root: TreeNode) -> int:
            if not root:
                return 0

            val = 0
            # 偷下一家
            if root.left:
                left_left_val = deep(root.left.left)
                left_right_val = deep(root.left.right)
                val += left_left_val
                val += left_right_val
            if root.right:
                right_left_val = deep(root.right.left)
                right_right_val = deep(root.right.right)
                val += right_left_val
                val += right_right_val

            val += root.val

            return max(val, deep(root.left) + deep(root.right))
        return deep(root)