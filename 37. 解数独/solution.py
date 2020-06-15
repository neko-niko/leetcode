from typing import List
from collections import defaultdict
import functools


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, N = 3, 9
        is_solved = False

        cols = [defaultdict(int) for i in range(N)]
        rows = [defaultdict(int) for i in range(N)]
        cells = [defaultdict(int) for i in range(N)]

        inner_cell_idx_func = lambda row, col: (row // 3) * 3 + col // 3
        cell_idx_func = functools.lru_cache()(inner_cell_idx_func)

        def place_num(num, i, j):
            rows[i][num] += 1
            cols[j][num] += 1
            cells[cell_idx_func(i, j)][num] += 1
            board[i][j] = str(num)

        def remove_num(num, i, j):
            del rows[i][num]
            del cols[j][num]
            del cells[cell_idx_func(i, j)][num]
            board[i][j] = "."

        def can_place(num, i, j):
            return (num not in rows[i]) and (num not in cols[j]) and (num not in cells[cell_idx_func(i, j)])

        def next_solve(row, col):
            if row == N - 1 and col == N - 1:
                nonlocal is_solved
                is_solved = True
                return

            if col == N - 1:
                solve(row + 1, 0)
            else:
                solve(row, col + 1)

        def solve(row, col):

            if board[row][col] == ".":
                for num in range(1, 10):
                    if can_place(num, row, col):
                        place_num(num, row, col)

                        next_solve(row, col)

                        if not is_solved:
                            remove_num(num, row, col)

            else:
                next_solve(row, col)

        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    place_num(int(board[i][j]), i, j)

        solve(0, 0)
