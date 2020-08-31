from collections import defaultdict


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        s_len = len(s)
        if s_len == 1:
            return s

        sub_str_dct = defaultdict(lambda: 1e9)

        for pos in range(1, s_len):
            if pos <= s_len / 2:
                if 2 * pos + 1 <= s_len:
                    if s[:pos] == s[pos + 1: 2 * pos + 1][::-1]:
                        sub_str_dct[pos] = s_len - (2 * pos + 1)
                if s[:pos] == s[pos: 2*pos][::-1]:
                    sub_str_dct[pos] = min(sub_str_dct[pos], s_len - (2 * pos))
        default_len = s_len - 1
        for pos, sub_len in sub_str_dct.items():
            if sub_len < default_len:
                default_len = sub_len

        return s[s_len - default_len:s_len][::-1] + s


print(Solution().shortestPalindrome("aacecaaa"))
