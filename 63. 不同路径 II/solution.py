from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        col = len(obstacleGrid[0])
        row = len(obstacleGrid)

        if not obstacleGrid:
            return 0
        if not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 1

        for i1, i2 in enumerate(obstacleGrid):
            for j1, j2 in enumerate(i2):
                if j2 == 1:
                    dp[i1][j1] = 0
                    continue
                if i1 > 0 and j1 > 0:
                    dp[i1][j1] = dp[i1-1][j1] + dp[i1][j1-1]
                elif i1 > 0:
                    dp[i1][j1] = dp[i1-1][j1]
                elif j1 > 0:
                    dp[i1][j1] = dp[i1][j1-1]

        return dp[-1][-1]

print(Solution().uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))