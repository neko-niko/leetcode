# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

from typing import *

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for i in range(n)] for j in range(n)]
        c, j = 1, 0
        while True:
            for i in range(j, n - j):
                result[j][i] = c
                c += 1
            for i in range(j + 1, n - j):
                result[i][n - j - 1] = c
                c += 1
            for i in reversed(range(j, n - j - 1)):
                result[n - j - 1][i] = c
                c += 1
            for i in reversed(range(j + 1, n - j - 1)):
                print(c)
                result[i][j] = c
                c += 1
            if c == n * n + 1:
                break
            j += 1

        return result


Solution().generateMatrix(3)