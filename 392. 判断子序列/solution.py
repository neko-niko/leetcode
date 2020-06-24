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
