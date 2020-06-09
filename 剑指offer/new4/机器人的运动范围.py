# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
class Solution:
    def movingCount(self, threshold, rows, cols):
        visited = [[0 for _ in range(cols)] for x in range(rows)]
        result = self.verfication(threshold, rows, cols, 0, 0, visited)
        return result

    def verfication(self, threshold, rows, cols, row, col, visited):
        cot = 0
        if row >= 0 and col >= 0 and row < rows and col < cols and \
                (self.helpfunc(row) + self.helpfunc(col) <= threshold) and visited[row][col] == 0:
            visited[row][col] = 1
            cot = 1 + self.verfication(threshold, rows, cols, row + 1, col, visited) + \
                  self.verfication(threshold, rows, cols, row - 1, col, visited) + \
                  self.verfication(threshold, rows, cols, row, col + 1, visited) + \
                  self.verfication(threshold, rows, cols, row, col - 1, visited)
        return cot

    def helpfunc(self, num):
        cot = 0
        while num:
            cot += num % 10
            num = num // 10
        return cot
Solution().movingCount(5, 10, 10)