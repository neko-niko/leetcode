from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0

        def inner_func(nums: List[int]) -> List[int]:
            if not nums or len(nums) == 1:
                return nums
            midd = len(nums) // 2
            left_list = inner_func(nums[0: midd])
            right_list = inner_func(nums[midd:])

            left_ptr = right_ptr = 0

            ret_list = []
            nonlocal res
            while left_ptr < len(left_list) and right_ptr < len(right_list):
                if left_list[left_ptr] <= right_list[right_ptr]:
                    ret_list.append(left_list[left_ptr])
                    res += right_ptr
                    left_ptr += 1
                else:
                    ret_list.append(right_list[right_ptr])
                    right_ptr += 1

            if left_ptr < len(left_list):
                ret_list += left_list[left_ptr:]
                res += (len(right_list) * (len(left_list) - left_ptr))
            if right_ptr < len(right_list):
                ret_list += right_list[right_ptr:]

            return ret_list

        inner_func(nums)
        return res


print(Solution().reversePairs([7,5,6,4]))