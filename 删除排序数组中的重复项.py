
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
# 快慢指针

from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ptr1 = ptr2 = 0
        len_nums = len(nums)
        while ptr2 < len_nums:
            while ptr2 < len_nums - 1 and nums[ptr2] == nums[ptr2 + 1] :
                ptr2 += 1
            nums[ptr1] = nums[ptr2]
            ptr2 += 1
            ptr1 += 1
        return ptr1
