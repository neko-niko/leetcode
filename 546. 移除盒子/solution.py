from typing import List
import math

# 区间dp

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        dct = {}

        def deep(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            if (l, r, k) in dct:
                return dct[(l, r, k)]

            while r > 1 and boxes[r] == boxes[r - 1]:
                k += 1
                r -= 1

            # 计算将后k(上面计算得出, 与当前数组最后一位连续相同的数的个数) + 1(当前数组最后一位) 进行平方的结果
            # 之后将l到r-1递归单独计算相加
            tmp = deep(l, r-1, 0) + math.pow(k+1, 2)

            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    # 可以视作将最后一位和前面的与最后一位相同的数, 将中间的数组扣去(计算中间数组的结果)后与计算扣去中间数组后, 后k+1个数字与前面的数字的子结果的和
                    tmp = max(tmp, deep(l, i, k+1) + deep(i+1, r-1, 0))
            dct[(l, r, k)] = tmp
            return tmp

        return int(deep(0, len(boxes)-1, 0))

print(Solution().removeBoxes([1,3,2,2,2,3,4,3,1]))