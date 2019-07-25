# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
# 说明:
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
from typing import *

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:     #把自己作为hash表
        n_len = len(nums)
        if not nums or 1 not in nums:
            return 1
        if n_len == 1:
            return 2
        for i in range(n_len):
            if nums[i] > n_len or nums[i] <= 0:
                nums[i] = 1

        for i in range(n_len):
            temp = abs(nums[i])
            if nums[temp-1] < 0:
                continue
            nums[temp-1] = -nums[temp-1]

        for i in range(n_len):
            if nums[i] <= 0:
                continue
            return i + 1
        return n_len+1


