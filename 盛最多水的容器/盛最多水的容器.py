# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。

from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:

        ptr1 = 0
        ptr2 = len(height) - 1
        max_capacity = (ptr2 - ptr1) * (min(height[ptr1], height[ptr2]))
        while ptr2 > ptr1:
            if height[ptr2] > height[ptr1]:
                ptr1 += 1
            else:
                ptr2 -= 1

            if (ptr2 - ptr1) * min(height[ptr1], height[ptr2]) > max_capacity:
                max_capacity = (ptr2 - ptr1) * min(height[ptr1], height[ptr2])

        return max_capacity