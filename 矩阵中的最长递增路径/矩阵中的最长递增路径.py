# 给定一个整数矩阵，找出最长递增路径的长度。
#
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
#
# 示例 1:
#
# 输入: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# 输出: 4
# 解释: 最长递增路径为 [1, 2, 6, 9]。
# 示例 2:
#
# 输入: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# 输出: 4
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
from typing import *

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        visted = [[0 for i in matrix[0]] for j in matrix]
        r_len = len(matrix)
        c_len = len(matrix[0])

        def judge(i, j, val):
            if i >=0 and j >= 0 and i < r_len and j < c_len and matrix[i][j] > val:
                return True
            else:
                return False

        def helper(i, j):
            if visted[i][j] != 0:
                return visted[i][j]
            temp = 1
            if judge(i+1, j, matrix[i][j]):
                temp = max(temp, 1+helper(i+1, j))
            if judge(i-1, j, matrix[i][j]):
                temp = max(temp, 1+helper(i-1, j))
            if judge(i, j+1, matrix[i][j]):
                temp = max(temp, 1+helper(i, j+1))
            if judge(i, j-1, matrix[i][j]):
                temp = max(temp, 1+helper(i, j-1))
            visted[i][j] = temp
            return temp
        res = 0
        for i in range(r_len):
            for j in range(c_len):
                res = max(res, helper(i, j))
        return res






print(Solution().longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
]  ))