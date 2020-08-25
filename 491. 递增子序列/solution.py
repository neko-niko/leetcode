from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        s = set()

        def deep(pos: int, tmp: List[int]):
            if pos == len(nums):
                if len(tmp) < 2:
                    return
                for i in range(1, len(tmp)):
                    if tmp[i - 1] > tmp[i]:
                        return
                if tuple(tmp) not in s:
                    res.append(tmp)
                    s.add(tuple(tmp))
            else:
                deep(pos + 1, tmp)
                deep(pos + 1, tmp + [nums[pos]])

        deep(0, [])

        return res


print(Solution().findSubsequences([4, 6, 7, 7]))
