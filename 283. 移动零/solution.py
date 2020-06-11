from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_len = len(nums)
        if nums_len < 2:
            return

        left_index = 0

        for i in range(nums_len):
            if nums[i] != 0:
                nums[left_index], nums[i] = nums[i], nums[left_index]
                left_index += 1


Solution().moveZeroes([0,1,0,3,12])