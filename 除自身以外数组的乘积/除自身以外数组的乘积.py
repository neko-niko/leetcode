# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

from typing import *

class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            nums_len = len(nums)
            p = 1
            result = []
            for i in range(nums_len):
                result.append(p)
                p *= nums[i]

            p = 1
            for i in reversed(range(nums_len)):
                result[i] *= p
                p *= nums[i]
            return result



if __name__ == '__main__':
    # Solution().productExceptSelf(range(1, 6))
    pass