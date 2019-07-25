# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。


from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 分治归并
        def helper1(left, right):
            if left > right:
                return 0
            else:
                min_ptr = left
                for i in range(left, right+1):
                    if heights[i] < heights[min_ptr]:
                        min_ptr = i

                return max(heights[min_ptr] * (right - left + 1), helper1(left, min_ptr - 1), helper1(min_ptr+1, right))

        stack = []
        def helper2():      #栈
            stack.append(-1)
            max_size = 0
            for i in range(0, len(heights)):
                while (stack[-1] != -1 and heights[i] < heights[stack[-1]]):
                    max_size = max(max_size, (heights[stack.pop()] * (i - stack[-1] - 1)))
                stack.append(i)
            while (stack[-1] != -1):
                max_size = max(max_size, (heights[stack.pop()] * (len(heights) - stack[-1] - 1)))
            return max_size
        return helper2()




print(Solution().largestRectangleArea([2,1,5,6,2,3]))
# [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]

