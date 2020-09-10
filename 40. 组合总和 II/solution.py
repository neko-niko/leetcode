from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        c_len = len(candidates)
        def deep(cur_lst, target, pos):
            if target == 0:
                res.append(cur_lst)
                return

            if target < 0 or pos >= c_len:
                return

            left = right = pos
            while right < c_len and candidates[left] == candidates[right]:
                right += 1

            tmp = []
            tmp_sum = 0
            for i in range(left, right):
                val = candidates[left]
                tmp.append(val)
                tmp_sum += val
                if target - tmp_sum < 0:
                    break
                deep(cur_lst + tmp, target-tmp_sum, right)

            deep(cur_lst, target, right)

        deep([], target, 0)
        return res

print(Solution().combinationSum2(candidates = [2,5,2,1,2], target = 5))
