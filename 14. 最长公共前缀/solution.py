from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        n = len(strs[0])
        if not n:
            return ""

        for substr in strs[1:]:
            str_len = len(substr)
            n = min(str_len, n)
            idx = 0
            while idx < n:
                if substr[idx] != strs[0][idx]:
                    n = idx
                    break
                idx += 1
        return n


print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
