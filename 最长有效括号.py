# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"


from typing import *

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        s_len = len(s)
        if s_len == 0:
            return 0


        def helper1():      #dp
            max_ = 0
            dp = [0] * s_len
            for i in range(1, s_len):
                if s[i] == '(':
                    dp[i] = 0
                else:
                    if s[i-1] == '(' and i-1 >= 0:
                        dp[i] = dp[i-2] + 2
                    elif s[i-1] == ')' and s[i - dp[i-1] - 1] == '(' and i - dp[i-1] - 1 >= 0:
                        dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
                max_ = max(dp[i], max_)
            return max_

        return helper1()