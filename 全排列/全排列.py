# 给定一个没有重复数字的序列，返回其所有可能的全排列。

from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def solution(result: list, nums: list, nums2: list):
            if len(nums) == 0:
                result.append(nums2)
            else:
                for i in range(len(nums)):
                    solution(result, nums[: i] + nums[i + 1:], nums2 + [nums[i]])

        result = []
        solution(result, nums, [])
        return result

    def permute2(self, nums: List[int]) -> List[List[int]]:

        def solution(result: list, nums: list, start: int):
            if start == len(nums):
                result.append(list(nums))
            for i in range(start, len(nums)):
                print(start, i)

                nums[i], nums[start] = nums[start], nums[i]
                solution(result, nums, start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        result = []
        solution(result, nums, 0)
        return result


print(Solution().permute2(list(range(2))))
