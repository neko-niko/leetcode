# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = max_right = 0
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if max_left > height[left]:
                    res += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if max_right > height[right]:
                    res += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
        return res

    def trap(self, height: List[int]):
        max_left = max_right = 0
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1
        return res
