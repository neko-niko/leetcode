# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        res = []

        def helper(root: TreeNode):
            if not root:
                return True
            res1 = helper(root.left)
            if res:
                if res[-1] <= root.val:
                    res.append(root.val)
                else:
                    return False
            else:
                res.append(root.val)

            return (res1 or helper(root.right))
        return helper(root)

