from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        for word in strs[1:]:
            idx = 0
            n = min(len(prefix), len(word))
            while idx < n:
                if prefix[idx] != word[idx]:
                    break
                idx += 1

            prefix = prefix[:idx]

        return prefix


print(Solution().longestCommonPrefix(["dog","racecar","car"]))
