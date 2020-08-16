from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image

        row = len(image)
        col = len(image[0])
        if not col:
            return image
        if sr < 0 or sc < 0 or sr > row or sc > col:
            return image

        visited = [[0] * col for _ in range(row)]
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
        s_color = image[sr][sc]
        def deep(r, c):
            visited[r][c] = 1
            if image[r][c] != s_color:
                return
            image[r][c] = newColor

            for inrc_r, incr_c in steps:
                next_r, next_c = inrc_r + r, incr_c + c
                if next_r < row and next_c < col and next_r >= 0 and next_c >= 0 and not visited[next_r][next_c]:
                    deep(next_r, next_c)

        deep(sr, sc)
        return image

print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))