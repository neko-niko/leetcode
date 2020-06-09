# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。


from typing import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in hash_set:
                temp = 0
                while i in hash_set:
                    temp += 1
                    i += 1
                if temp > res: res = temp
        return res

    def longestConsecutive2(self, nums: List[int]) -> int:
        cot_dct = {}
        res = 0
        for i in nums:
            if i not in cot_dct:

                left = cot_dct.get(i-1, 0)
                right = cot_dct.get(i+1, 0)
                temp = 1 + left + right
                if temp > res: res = temp
                cot_dct[i] = temp
                cot_dct[i-left] = temp
                cot_dct[i+right] = temp

        return res


