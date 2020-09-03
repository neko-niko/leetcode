from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [-1] * n
        int_res: List[List[int]] = []
        res: List[List[str]] = []

        def deep(t):
            if t >= n:
                int_res.append(list(matrix))
                return

            for row in range(n):
                if matrix[row] != -1:
                    continue
                for col in range(n):
                    if col in matrix:
                        continue
                    for r, c in enumerate(matrix[:row]):
                        if c == -1 or abs(r - row) == abs(c - col):
                            break
                    else:
                        matrix[row] = col
                        deep(t + 1)
                        matrix[row] = -1

        deep(0)

        def trans_to_str(int_lst: List[int]) -> List[str]:
            ret = []
            for col in int_lst:
                tmp = ['Q' if pos == col else '.' for pos in range(n)]
                ret.append(''.join(tmp))
            return ret

        for t in int_res:
            res.append(trans_to_str(t))

        return res


print(Solution().solveNQueens(4))
