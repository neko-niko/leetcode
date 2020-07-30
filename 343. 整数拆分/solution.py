import math


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        remainder, divisor = n % 3, n // 3
        if remainder == 0:
            return int(math.pow(3, divisor))
        elif remainder == 1:
            return int(math.pow(3, divisor - 1)) * 4
        else:
            return int(math.pow(3, divisor)) * 2
