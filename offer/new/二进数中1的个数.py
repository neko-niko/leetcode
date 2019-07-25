class Solution:
    def NumberOf1(self, n):
        cot = 0

        while n != 0:
            cot += 1
            n = n & (n - 1)
        return cot


print(Solution().NumberOf1(-111))