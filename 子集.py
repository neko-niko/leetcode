# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
from typing import *

# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def solution(result: list, nums: list, nums2: list):
            result.append(nums2)
            if nums:
                for i in range(len(nums)):
                    solution(result, nums[i + 1: ], nums2 + [nums[i]])

        result = []
        solution(result, nums, [])
        print(len(result))

Solution().subsets([1, 2, 3, 4])

