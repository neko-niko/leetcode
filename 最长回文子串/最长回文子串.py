# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
import time
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #
        end = start = 0
        s_len = len(s)
        for i in range(s_len):
            len1 = self.longest(s, i, i)
            len2 = self.longest(s, i, i+1)
            result = max(len1, len2)
            # print(result)
            if result > end - start + 1:
                if result % 2 == 1:
                    end = i + (result - 1) // 2
                    start = i - (result - 1) // 2
                else:
                    end = i + result // 2
                    start = i - result // 2 + 1

        # print(start, end)
        return s[start: end+1]

    def longest(self, s, left, right) -> int:
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                left += 1
                right -= 1
                return right - left + 1
        left += 1
        right -= 1

        return right - left + 1




class Solution2(object):
    def Managcher(self, s: str):
        ptr = max_len = id = mx = 0

        lst = []
        lst.append('$')
        for i in s:
            lst.append('#')
            lst.append(i)
        lst.append('#')
        lst.append('\0')

        p = [0 for i in range(len(lst))]
        for i in range(1, len(lst) - 1):
            if i < mx:
                p[i] = min(mx - i, p[2*id - i])
            else:
                p[i] = 1
            while lst[i - p[i]] == lst[i + p[i]]:
                p[i] += 1

            if i + p[i] > mx:
                id = i
                mx = i + p[i]
            if p[i] - 1 > max_len:
                max_len = p[i] - 1
                ptr = i
        # print(max_len, ptr)
        return ''.join(lst[ptr-max_len: ptr+max_len]).replace('#', '')







if __name__ == '__main__':
    time1 = time.time()

    print(Solution2().Managcher(''.join(['ab' for i in range(500)])))
    print(time.time() - time1)
    time2 = time.time()
    print(Solution().longestPalindrome("babad"))
    print(time.time() - time2)