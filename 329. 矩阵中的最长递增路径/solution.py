from typing import List, Dict, Tuple
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        row_len = len(matrix)
        if not row_len:
            return 0
        col_len = len(matrix[0])
        if not col_len:
            return 0

        # cache: Dict[Tuple[int, int], int] = {}

        step = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValid(val: int, r: int, c: int) -> bool:
            if r >= row_len or c >= col_len or r < 0 or c < 0 or matrix[r][c] >= val:
                return False
            return True

        @lru_cache(1024)
        def deep(r: int, c: int) -> int:
            # if (r, c) in cache:
            #     return cache[(r, c)]

            tmp = 1

            for r_s, c_s in step:
                if isValid(matrix[r][c], r+r_s, c+c_s):
                    tmp = max(tmp, 1+deep(r+r_s, c+c_s))

            # cache[(r, c)] = tmp
            return tmp

        res = -1
        for r in range(row_len):
            for c in range(col_len):
                res = max(res, deep(r, c))

        return res

print(Solution().longestIncreasingPath([
  [9,9,4],
  [6,6,8],
  [2,1,1]
] ))