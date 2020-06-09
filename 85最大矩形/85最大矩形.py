# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例:
#
# 输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6

from typing import *


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def helper(heights: list):
            stack = []
            maxarea = 0
            stack.append(-1)
            for i in range(len(heights)):
                while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                    maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
                stack.append(i)
            while stack[-1] != -1:
                maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
            return maxarea

        if not matrix:
            return 0
        dp = [0 for i in range(len(matrix[0]))]

        maxarea = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            print(dp)

            maxarea = max(maxarea, helper(dp))

        return maxarea

    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        left = [0 for _ in matrix[0]]
        right = [n for _ in matrix[0]]
        height = [0 for _ in matrix[0]]
        maxarea = 0
        for i in range(len(matrix)):
            cur_left = 0
            cut_right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] = height[j] + 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    cur_left = j + 1
                    left[j] = 0
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cut_right)
                else:
                    cut_right = j
                    right[j] = n
            for j in range(n):
                maxarea = max(maxarea, height[j]*(right[j]-left[j]))
        return maxarea


Solution().maximalRectangle([["1", "0", "1", "0", "0"],
                             ["1", "0", "1", "1", "1"],
                             ["1", "1", "1", "1", "1"],
                             ["1", "0", "0", "1", "0"]]
                            )
