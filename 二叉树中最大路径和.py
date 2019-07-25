class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = int(-1e13)

    def maxPathSum(self, root: TreeNode) -> int:

        self.core(root)
        return self.result


    def core(self, root: TreeNode):
        if root is None:
            return 0
        maxleft = self.core(root.left)
        maxright = self.core(root.right)

        max_value = max(root.val, root.val + maxleft, root.val + maxright, root.val + maxright + maxleft)
        if max_value > self.result:
            self.result = max_value

        return max_value


# if __name__ == '__main__':
    # print(Solution().lst_maxsum([-1, 1, -2, 3, 1, -2, -3]))
