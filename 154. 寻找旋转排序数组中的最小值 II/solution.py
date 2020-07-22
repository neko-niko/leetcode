from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            midd = (left + right) // 2
            if nums[midd] > nums[right]:
                left = midd + 1
            elif nums[midd] < nums[right]:
                right = midd
            else:
                left += 1
        return nums[left]


print(Solution().findMin([1,3,5]))