class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        ptr_s = ptr_t = 0
        len_s, len_t = len(s), len(t)
        while ptr_t < len_t:
            if s[ptr_s] == t[ptr_t]:
                ptr_t += 1
                ptr_s += 1
            else:
                ptr_t += 1

            if ptr_s == len_s:
                return True

        return False

    def isSubSequence_dp(self, s: str, t: str) -> bool:
        from collections import defaultdict
        t_len = len(t)

        dp = [defaultdict(lambda: t_len+1) for _ in range(t_len+1)]
        char_list = list(map(chr, [ord('a') + i for i in range(26)]))

        for c in char_list:
            for i in reversed(range(t_len)):
                if t[i] == c:
                    dp[i][c] = i
                else:
                    dp[i][c] = dp[i + 1][c]

        # print(dp)

        pos = 0
        for c in s:
            if dp[pos][c] == t_len + 1:
                return False
            else:
                pos = dp[pos][c] + 1
        return True

print(Solution().isSubSequence_dp("aaaaaa",
"bbaaaa"))
