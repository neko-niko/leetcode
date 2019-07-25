from typing import *

# 情况1 不绕圈
class Solution:
    def rob(self, nums: List[int]) -> int:
        res = []
        n_len = len(nums)
        if n_len == 0:
            return 0
        if n_len == 1:
            return nums[0]

        res_append = res.append
        res_append(nums[0])
        for i in range(1, n_len):
            if i == 1:
                res_append(max(nums[i], nums[i-1]))
            else:
                res_append(max(res[i-2] + nums[i], res[i-1]))
        return max(res)


# 情况2 绕圈
class Solution:
    def rob(self, nums: List[int]) -> int:
        res1 = []
        res2 = []
        n_len = len(nums)
        if n_len == 0:
            return 0
        if n_len == 1:
            return nums[0]
        if n_len == 2:
            return max(nums)
        res1.append(nums[0])
        res2.append(0)
        for i in range(1, n_len-1):
            if i == 1:
                res1.append(max(nums[1], res1[0]))
            else:
                res1.append(max(res1[i-2]+nums[i], res1[i-1]))
        for i in range(1, n_len):
            if i == 1:
                res2.append(nums[i])
            else:
                res2.append(max(nums[i] + res2[i-2], res2[i-1]))

        return max(max(res1), max(res2))


#情况3 树状

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.look = {}


    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in self.look:
            return self.look[root]
        val = 0


        if root.left:
            val += self.rob(root.left.left)
            val += self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.right)
            val += self.rob(root.right.left)

        val += root.val
        val = max(val, self.rob(root.left)+self.rob(root.right))
        self.look[root] = val
        return val


