# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#

from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n_len = len(nums)
        if not n_len or n_len == 1:
            return

        i = n_len - 1
        while nums[i] <= nums[i-1] and i > 0:
            i -= 1

        if i == 0:
            self.myreversed(0, n_len - 1, nums)
        else:
            j = i
            i = i - 1
            temp = 1 << 63
            for k in range(j, n_len):
                if nums[k] - nums[i] >= 0 and nums[k] - nums[i] < temp:
                    temp = nums[k] - nums[i]
                    j = k
            nums[i], nums[j] = nums[j], nums[i]

            self.myreversed(i+1, n_len-1, nums)

    def myreversed(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



print(Solution().nextPermutation([1,2,3]))