# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 说明：
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:     #滑动窗口
        from collections import Counter
        s_len = len(s)
        t_len = len(t)
        if not s_len or s_len < t_len:
            return ''


        target = Counter(list(t))

        min_len = 1e13
        res_l = 0
        res_r = 0
        left = right = 0

        while right < s_len:
            character = s[right]
            if character in target:
                target[character] -= 1
                while all(map(lambda i: i <= 0, target.values())) and left < right:
                    temp = s[left]
                    if left - right + 1 < min_len:
                        min_len = right - left + 1
                        res_l = left
                        res_r = right
                    if temp in target:
                        target[temp] += 1
                    left += 1
            right += 1

        return '' if min_len == 1e13 else s[res_l: res_r+1]

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
