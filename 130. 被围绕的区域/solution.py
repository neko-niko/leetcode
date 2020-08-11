from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row = len(board)
        col = len(board[0])
        visited = [[0]*col for _ in range(row)]
        step_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def deep1(r: int, c: int):
            if board[r][c] != 'O' or visited[r][c] != 0:
                return
            visited[r][c] = -1
            for x, y in step_list:
                next_row = r + x
                next_col = c + y
                if next_row >= 0 and next_col >= 0 and next_row < row and next_col < col and visited[next_row][next_col] == 0:
                   deep1(next_row, next_col)

        for pos in range(col):
            if board[0][pos] == 'O':
                deep1(0, pos)
            if board[-1][pos] == 'O':
                deep1(row-1, pos)

        for pos in range(1, row-1):
            if board[pos][0] == 'O':
                deep1(pos, 0)
            if board[pos][-1] == 'O':
                deep1(pos, col-1)

        for r in range(row):
            r1 = board[r]
            r1_v = visited[r]
            for c in range(col):
                if r1_v[c] == -1:
                    r1[c] = 'O'
                else:
                    r1[c] = 'X'

print(Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))