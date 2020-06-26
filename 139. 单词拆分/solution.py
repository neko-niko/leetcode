from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        if not wordDict:
            return False

        wordDict = set(wordDict)

        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]


print(Solution().wordBreak())
