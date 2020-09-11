from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def deep(target, cur, lst: list):
            if target == 0 and len(lst) == k:
                res.append(lst)
                return
            lst_len = len(lst)

            if 10-cur < k - lst_len or target < 0 or cur >= 10:
                return

            deep(target-cur, cur + 1, lst+[cur])
            deep(target, cur + 1, lst)

        deep(n, 1, [])

        return res

    def combinationSum3_deep(self, k: int, n: int) -> List[List[int]]:
        candidate_set = set(range(1, 10))
        res = []

        def solve(n, lst: list):
            if n == 0 and len(lst) == k:
                item_lst = sorted(lst)
                if item_lst not in res:
                    res.append(item_lst)
                return

            if len(lst) >= k:
                return

            for num in range(1, 10):
                if num in candidate_set and n - num >= 0 and (len(lst) == 0 or num > lst[-1]):
                    candidate_set.remove(num)

                    lst.append(num)
                    solve(n - num, lst)

                    candidate_set.add(num)
                    lst.pop()

        solve(n, [])
        return res


print(Solution().combinationSum3(3, 9))