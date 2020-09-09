from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        dp = [[] for i in range(target + 1)]
        dp[0] = [[]]
        for num in candidates:
            for i in range(num, target + 1):
                if dp[i - num]:
                    for lst in dp[i - num]:
                        dp[i].append(lst + [num])

        return dp[target]

    def combinationSum_deep(self, candidates, target):

        res = []
        len_c = len(candidates)

        def deep(cur_lst, cur_val, pos):
            if cur_val > target or pos >= len_c:
                return
            if cur_val == target:
                res.append(cur_lst)
                return

            pos_val = candidates[pos]
            deep(cur_lst, cur_val, pos + 1)
            deep(cur_lst + [pos_val], cur_val + pos_val, pos_val)


print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
