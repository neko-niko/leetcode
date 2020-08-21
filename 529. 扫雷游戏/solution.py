from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        c_r, c_c = click[0], click[1]
        row, col = len(board), len(board[0])
        if c_r >= row or c_c >= col:
            return board
        if board[c_r][c_c] == "M":
            board[c_r][c_c] = "X"
            return board

        step = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]

        def deep(r: int, c: int):
            if board[r][c] != "E":
                return

            cot = 0
            can_next = []
            for step_r, step_c in step:
                next_r, next_c = step_r + r, step_c + c
                if next_r < 0 or next_r >= row or next_c < 0 or next_c >= col:
                    continue
                if board[next_r][next_c] == "M":
                    cot += 1
                elif board[next_r][next_c] == "E":
                    can_next.append((next_r, next_c))

            if cot > 0:
                board[r][c] = str(cot)
            else:
                board[r][c] = "B"

            if not cot:
                for deep_r, deep_c in can_next:
                    deep(deep_r, deep_c)

        deep(c_r, c_c)
        return board


print(Solution().updateBoard([['E', 'E', 'E', 'E', 'E'],
                              ['E', 'E', 'M', 'E', 'E'],
                              ['E', 'E', 'E', 'E', 'E'],
                              ['E', 'E', 'E', 'E', 'E']], [3, 0]))
