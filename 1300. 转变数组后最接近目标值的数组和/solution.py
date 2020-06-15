from typing import List
import bisect
import dis

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        arr.sort()
        pre_sum = [0]
        for num in arr:
            pre_sum.append(pre_sum[-1] + num)
        left, right, temp = 0, max(arr), -1

        while left <= right:
            midd = (left + right) // 2

            pos = bisect.bisect_left(arr, midd)
            cur = pre_sum[pos] + (len(arr) - pos) * midd
            if cur <= target:
                temp = midd
                left = midd + 1
            else:
                right = midd - 1

        small_pos = bisect.bisect_left(arr, temp)
        small_sum = pre_sum[small_pos] + (len(arr) - small_pos) * temp

        big_pos = bisect.bisect_left(arr, temp + 1)
        big_sum = pre_sum[big_pos] + (len(arr) - big_pos) * (temp + 1)

        return temp if abs(small_sum - target) <= abs(big_sum - target) else temp + 1



