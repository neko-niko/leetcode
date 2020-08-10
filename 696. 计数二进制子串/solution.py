class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0

        tmp, cot = 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                tmp += 1
            else:
                cot = tmp
                tmp = 1
            if cot >= tmp:
                res += 1

        return res


print(Solution().countBinarySubstrings("00110011"))


