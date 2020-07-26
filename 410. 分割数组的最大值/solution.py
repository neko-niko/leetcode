from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        nums_len = len(nums)
        prefix = [0] * (nums_len + 1)

        for i in range(nums_len):
            prefix[i + 1] = prefix[i] + nums[i]

        dp = [[1 << 32] * (m+1) for i in range(nums_len+1)]
        dp[0][0] = 0
        for i in range(1, nums_len+1):
            for j in range(1, min(i, m)+1):
                for k in range(i):
                    # 将前i个数分为j个数组的j个数组中最大值的最小值为
                    # 将当前的最后k个数划分为一个单独的数组, 求将前i-k个数分为j-1的数组的结果(前i-k个数分为j-1个数组的数组和的最大值的最小值)和这k个数的和的最大值
                    # 遍历k, 选取最小的情况
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], prefix[i]-prefix[k]))
        return dp[nums_len][m]

print(Solution().splitArray([1, 2], 2))

