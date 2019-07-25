from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        from functools import reduce
        return reduce(lambda r, x: (max(r[0], r[1] + x), max(x, r[1] + x)), nums, initial=(max(nums), 0))[0]

