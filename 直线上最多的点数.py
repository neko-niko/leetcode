from typing import *


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def max_point_on_a_line(i):
            duplicates = 0
            lines = {}
            y_equal = 1
            count = 1

            def get_line(i, j, duplucates, count):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                if x1 == x2 and y1 == y2:
                    duplucates += 1
                elif y1 == y2:
                    nonlocal y_equal
                    y_equal += 1
                    count = max(y_equal, count)
                else:
                    slope = (x1 - x2) / (y1 - y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope], count)

                return duplucates, count

            for j in range(i+1, len(points)):
                duplicates, count = get_line(i, j, duplicates, count)
            return count + duplicates
        if len(points) <= 2:
            return len(points)
        else:
            max_point = 1
            for i in range(len(points) - 1):
                max_point = max(max_point, max_point_on_a_line(i))
            return max_point

