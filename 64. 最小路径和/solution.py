from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        # 基本dp, 可优化空间使用一维数组
        dp = [[0 for j in range(col)] for i in range(row)]

        dp_row_0 = dp[0]
        grid_row_0 = grid[0]
        dp_row_0[0] = grid_row_0[0]
        for i in range(1, col):
            dp_row_0[i] = dp_row_0[i - 1] + grid_row_0[i]

        for i in range(1, row):
            for j in range(col):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]

