from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        next_arr = self.get_next_arr(s)

        ptr_s = ptr_t = 0

        while ptr_t < len(t):
            if ptr_s == -1:
                ptr_t += 1

            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
                ptr_t += 1
            else:
                ptr_s = next_arr[ptr_s]

            if ptr_s == len(s):
                return True
        return False

    def get_next_arr(self, s: str) -> List[int]:
        len_s = len(s)

        if len_s == 0:
            return []

        ptr = 0
        res = [-1]
        cur = -1

        while ptr < len_s - 1:
            if cur == -1 or s[cur] == s[ptr]:
                cur += 1
                res.append(cur)
                ptr += 1
            else:
                cur = res[cur]

        return res


print(Solution().isSubsequence('abc', 'ahbgabcad'))
