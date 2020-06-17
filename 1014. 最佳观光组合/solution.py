from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        len_a = len(A)
        if len_a <= 1:
            return 0

        max_pre = A[0]

        max_val = -1

        j = 1
        while j < len_a:

            cur_val = max_pre + A[j] - j
            if cur_val > max_val:
                max_val = cur_val

            max_pre = max(max_pre, A[j]+j)
            j += 1

        return max_val


print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))