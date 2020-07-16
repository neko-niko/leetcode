from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.intersect_sort(nums1, nums2)

        small_list, big_list = nums1, nums2
        if len(small_list) > len(big_list):
            small_list, big_list = big_list, small_list

        cot_dict = Counter(small_list)
        res = []
        for item in big_list:
            if item in cot_dict and cot_dict[item] > 0:
                res.append(item)
                cot_dict[item] -= 1
        return res

    def intersect_sort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ptr1 = ptr2 = 0
        res = []
        res_append = res.append
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                res_append(nums2[ptr2])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        return res





