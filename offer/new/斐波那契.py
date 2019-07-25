class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            lst = [0, 1]
            [lst.append(lst[x-1] + lst[x-2]) for x in range(2, n+1)]
            return lst[-1]

print(Solution().Fibonacci(39))