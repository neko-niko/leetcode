from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False

        r_len = len(board)
        c_len = len(board[0])

        visited = [[False] * c_len for _ in range(r_len)]

        def deep(pos, r, c) -> bool:
            if pos == len(word):
                return True
            if r < 0 or r >= r_len or c < 0 or c >= c_len or visited[r][c]:
                return False

            row = board[r]
            if row[c] == word[pos]:
                visited[r][c] = True
                val = deep(pos + 1, r + 1, c) or \
                      deep(pos + 1, r - 1, c) or \
                      deep(pos + 1, r, c + 1) or \
                      deep(pos + 1, r, c - 1)
                visited[r][c] = False
                return val

            return False

        for r in range(r_len):
            for c in range(c_len):
                if deep(0, r, c):
                    return True

        return False

print(Solution().exist(board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],word="ABCB"))