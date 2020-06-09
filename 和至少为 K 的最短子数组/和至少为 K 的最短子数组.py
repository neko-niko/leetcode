from typing import *



class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        result = -1
        a_len = len(A)
        sum_a = 0
        pre = 0

        for i in range(a_len):
            if A[i] > K:
                return 1
            sum_a += A[i]
            if sum_a < 1:
                pre = i + 1
                sum_a = 0
                continue
            j = i
            while A[j] < 0:
                A[j - 1] = A[j - 1] +A[j]
                A[j] = 0
                j -= 1
            if sum_a >= K:
                while sum_a - A[pre] > K:
                    sum_a -= A[pre]
                    pre += 1
                if result == -1 or result > i - pre + 1:
                    result = i - pre + 1

        return result