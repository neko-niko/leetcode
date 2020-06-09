# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            flag = 1
            x = -x
        else:
            flag = 0

        result = 0
        while x:
            result *= 10
            result += x % 10
            x = x // 10
        result = -result if flag else result
        threshold = (1 << 31)
        if result > threshold or result < - (threshold - 1):
            return 0
        return result
