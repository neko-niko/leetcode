class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n == 0:
            return 0
        tmp = n
        cot = 0
        while tmp // 10 != 0:
            cot += 1
            tmp = tmp // 10
        high = pow(10, cot)
        if high == 1:
            return 1
        tmp = n
        base = self.count(high)
        if tmp == high:
            return base
        elif tmp < 2*high:
            count = base + self.NumberOf1Between1AndN_Solution(tmp%high) + tmp % high   # 小于等于high部分  递归非最高位部分  最高位部分出现次数
        else:
            count = (base - 1)*(tmp // high) + high + self.NumberOf1Between1AndN_Solution(tmp%high)
        return count

    def count(self, num):
        if num == 1:
            return 1
        if num == 10:
            return 2
        else:
            return 10 * (self.count(num//10)-1) + 1 + num // 10     # 非最高位部分 被10整除部分 最高位部分

print('resut:', Solution().NumberOf1Between1AndN_Solution(101))