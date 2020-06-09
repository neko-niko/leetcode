class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        row = len(matrix)
        if row == 0:
            return None
        col = len(matrix[0])
        if col == 0:
            return None
        if row == 1 or col == 1:
            return (matrix[0] if row == 1 else [x[0] for x in matrix])
        res = []
        i = 0
        while i*2 < col and i*2 < row:
            endX = col - 1 - i
            # print(endX)
            endY = row - 1 - i
            for j in range(i, endX+1):
                res.append(matrix[i][j])
            if endY > i:
                for j in range(i+1, endY+1):
                    res.append(matrix[j][endX])
            if i < endX and i < endY:
                for j in reversed([x for x in range(i, endX)]):
                    res.append(matrix[endY][j])

            if i < endX and i < endY - 1:
                for j in reversed([x for x in range(i+1, endY)]):
                    res.append(matrix[j][i])
            i += 1
        return res


if __name__ == '__main__':
    print(Solution().printMatrix([[1,2],[3,4],[5,6],[7,8],[9,10]]))