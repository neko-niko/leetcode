class Solution:
    def countSubstrings(self, s: str) -> int:
        cot = 0
        for i in range(2 * len(s) - 1):
            l = i // 2
            r = i // 2 + i % 2
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    cot += 1
                else:
                    break
        return cot


print(Solution().countSubstrings("fdsklf"))
