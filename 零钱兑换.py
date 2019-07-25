from typing import *

# 最少能够达到目标的硬币数
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [1e13 for i in range(amount + 1)]
        res[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if j > i:
                    break
                else:
                    res[i] = min(res[i-j] + 1, res[i])

        return res[-1] if res[-1] != 1e13 else -1



#能够达到目标的最多方法
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = [0 for i in range(amount + 1)]
        res[0] = 1
        coins.sort()

        for i in coins:
            for j in range(1, amount + 1):
                if i > j:
                    continue
                else:
                    res[j] = res[j] + res[j-i]
        return res[-1]

