from typing import List
from functools import lru_cache

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        dp = [[0]*nums_len for _ in range(nums_len)]
        for i in range(nums_len):
            dp[i][i] = nums[i]

        for i in range(nums_len-2, -1, -1):
            for j in range(i+1, nums_len):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][nums_len-1] >= 0

    def PredictTheWinner_deep(self, nums: List[int]) -> bool:

        @lru_cache(4096)
        def deep1(left: int, right: int, cur_player: bool, cur_val: int) -> int:
            if left == right:
                if cur_player:
                    return cur_val + nums[right]
                else:
                    return cur_val - nums[right]

            if cur_player:
                left_val = deep1(left + 1, right, not cur_player, cur_val + nums[left])
                right_val = deep1(left, right - 1, not cur_player, cur_val + nums[right])
                return max(left_val, right_val)
            else:
                left_val = deep1(left+1, right, not cur_player, cur_val - nums[left])
                right_val = deep1(left, right-1, not cur_player, cur_val - nums[right])
                return min(left_val, right_val)

        def deep2(left, right) -> int:
            if left == right:
                return nums[left]

            left_val = nums[left] - deep2(left+1, right)
            right_val = nums[right] - deep2(left, right-1)
            return max(left_val, right_val)

        # return deep1(0, len(nums)-1, True, 0) >= 0
        return deep2(0, len(nums)-1) >= 0

print(Solution().PredictTheWinner([1, 5, 233, 7]))
