# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
#
# 示例:
#
# 输入: [5,2,6,1]
# 输出: [2,1,1,0]
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.


from typing import *



#方法1 二叉搜索树
class TreeNode(object):
    def __init__(self, index, val):
        self.val = val
        self.index = index
        self.left_node = 0
        self.count = 0
        self.left: TreeNode = None
        self.right:TreeNode = None

    def insert(self, node):
        if node.val <= self.val:
            self.left_node += 1
            if not self.left:
                self.left = node
            else:
                self.left.insert(node)
        else:
            node.count += self.left_node + 1
            if not self.right:
                self.right = node
            else:
                self.right.insert(node)



class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        root = TreeNode(0, nums[0])
        for i in range(1, len(nums)):
            root.insert(TreeNode(i, nums[i]))

        res = [0] * len(nums)

        def dfs(root: TreeNode):
            if not root:
                return
            print(root.count)
            res[root.index] = root.count
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res[::-1]


class Solution2:        #归并
    def countSmaller(self, nums: List[int]) -> List[int]:

        n_len = len(nums)
        if not n_len:
            return []
        if n_len == 1:
            return [0]

        temp = [None for i in nums]
        res = [0 for i in nums]
        indexs = [i for i in range(n_len)]

        self.helper(nums, 0, n_len - 1, res, temp, indexs)

        return res



    def helper(self, nums, left, right, res, temp, indexs):
        if left == right:
            return

        mid = left + (right - left) // 2
        self.helper(nums, left, mid, res, temp, indexs)
        self.helper(nums, mid+1, right, res, temp, indexs)
        if nums[indexs[mid]] <= nums[indexs[mid+1]]:return
        self.core(res, temp, indexs, nums, left, right)



    def core(self, res, temp, indexs, nums, left, right):
        mid = left + (right - left) // 2
        for i in range(left, right + 1):
            temp[i] = indexs[i]

        l = left
        r = mid + 1
        for i in range(left, right+1):
            if l > mid:
                indexs[i] = temp[r]
                r += 1
            elif r > right:
                indexs[i] = temp[l]
                l += 1
                res[indexs[i]] += (r - mid)
            elif nums[temp[l]] <= nums[temp[r]]:
                indexs[i] = temp[l]
                l += 1
                res[indexs[i]] += (r - mid - 1)
            else:
                indexs[i] = temp[r]
                r += 1





Solution().countSmaller([5, 2, 6, 1])
class Solution:
    def countSmaller(self, nums):
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        temp = [None for _ in range(size)]
        indexes = [i for i in range(size)]
        res = [0 for _ in range(size)]

        self.__helper(nums, 0, size - 1, temp, indexes, res)
        return res

    def __helper(self, nums, left, right, temp, indexes, res):
        if left == right:
            return
        mid = left + (right - left) // 2

        # 计算一下左边
        self.__helper(nums, left, mid, temp, indexes, res)
        # 计算一下右边
        self.__helper(nums, mid + 1, right, temp, indexes, res)

        if nums[indexes[mid]] <= nums[indexes[mid + 1]]:
            return
        self.__sort_and_count_smaller(nums, left, mid, right, temp, indexes, res)

    def __sort_and_count_smaller(self, nums, left, mid, right, temp, indexes, res):
        # [left,mid] 前有序数组
        # [mid+1,right] 后有序数组

        # 先拷贝，再合并

        for i in range(left, right + 1):
            temp[i] = indexes[i]

        l = left
        r = mid + 1
        for i in range(left, right + 1):
            if l > mid:
                # l 用完，就拼命使用 r
                # [1,2,3,4] [5,6,7,8]
                indexes[i] = temp[r]
                r += 1
            elif r > right:
                # r 用完，就拼命使用 l
                # [6,7,8,9] [1,2,3,4]
                indexes[i] = temp[l]
                l += 1
                # 注意：此时前面剩下的数，比后面所有的数都大
                res[indexes[i]] += (right - mid)
            elif nums[temp[l]] <= nums[temp[r]]:
                # [3,5,7,9] [4,6,8,10]
                indexes[i] = temp[l]
                l += 1
                # 注意：
                res[indexes[i]] += (r - mid - 1)
            else:
                assert nums[temp[l]] > nums[temp[r]]
                # 上面两种情况只在其中一种统计就可以了
                # [3,5,7,9] [4,6,8,10]
                indexes[i] = temp[r]
                r += 1

