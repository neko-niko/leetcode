# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？

class Solution:
    def uniquePaths(self, m: int, n: int):
        matrix = [[0 for i in range(m)] for j in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                if i == 0 and j == 0:
                    matrix[0][0] = 1
                elif i == 0:
                    matrix[i][j] = matrix[i][j - 1]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        print(matrix)
        return matrix[n-1][m-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(7, 3))
