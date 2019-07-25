# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。


class Solution:
    def spiralOrder(self, matrix: list) -> list:
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        if col == 0:
            return []
        if col == 1 or row == 1:
            return matrix[0] if row == 1 else list(map(lambda x: x[0], matrix))

        i = 0
        res = []
        while i * 2 < col and i * 2 < row:
            endX = col - i - 1
            endY = row - i - 1
            for j in range(i, endX + 1):
                res.append(matrix[i][j])

            if endY > i:
                for j in range(i+1, endY + 1):
                    res.append(matrix[j][endX])

            if i < endX and i < endY:
                for j in reversed(range(i, endX)):
                    res.append(matrix[endY][j])

            if i + 1 < endY and i < endX:
                for j in reversed(range(i + 1, endY)):
                    res.append(matrix[j][i])
            i += 1
        return res
    def solution2(self, matrix: list):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[: : -1]
            if matrix and matrix[0]:
                for row in matrix[: : -1]:
                    res.append(row.pop(0))
        return res
