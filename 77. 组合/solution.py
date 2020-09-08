from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def deep(tmp_list):
            start = 0 if not tmp_list else tmp_list[-1]
            if len(tmp_list) + (n - start + 1) < k:
                return
            if len(tmp_list) == k:
                res.append(tmp_list)
                return

            for i in range(start + 1, n + 1):
                deep(tmp_list + [i])

        deep([])

        return res


print(Solution().combine(4, 3))
