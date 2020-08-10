from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n_len = len(nums)
        if n_len == 0:
            return 0
        if n_len == 1:
            return nums[0]
        val1, val2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if val1 + nums[i] > val2:
                tmp = val1
                val1 = val2
                val2 = tmp + nums[i]
            else:
                val1 = val2

        return max(val1, val2)