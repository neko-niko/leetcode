from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums_len = len(nums)

        for i in range(nums_len):
            if nums[i] > nums_len or nums[i] <= 0:
                nums[i] = -1

        pos = 0
        while pos < nums_len:
            if nums[pos] == -1 or nums[pos] == nums[nums[pos] - 1] or nums[pos] == pos + 1:
                pos += 1
                continue
            nums[nums[pos] - 1], nums[pos] = nums[pos], nums[nums[pos] - 1]

        for i, j in enumerate(nums):
            if i != j - 1:
                return i + 1

        return nums_len + 1


