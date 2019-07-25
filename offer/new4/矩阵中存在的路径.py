class Solution:
    def hasPath(self, matrix, rows, cols, path):
        beifen = [[0 for _ in range(cols)] for x in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.haspathcore(matrix, rows, cols, i, j, path, beifen):
                    return True

        return False



    def haspathcore(self, matrix, rows, cols, row, col, path, visited):
        if len(path) == 0:
            return True
        else:
            haspath = False
            if row >= 0 and row < rows and col >= 0 and col < cols and matrix[cols*row+col] == path[0] and visited[row][col] == 0:
                visited[row][col] = 1
                haspath = self.haspathcore(matrix, rows, cols, row + 1, col, path[1:], visited) or \
                          self.haspathcore(matrix, rows, cols, row - 1, col, path[1:], visited) or \
                          self.haspathcore(matrix, rows, cols, row, col - 1, path[1:], visited) or \
                          self.haspathcore(matrix, rows, cols, row, col + 1, path[1:], visited)
                if not haspath:
                    visited[row][col] = 0
            return haspath

