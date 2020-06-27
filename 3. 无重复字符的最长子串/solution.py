class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        char_pos_record = {}

        left = res = 0

        for i, char in enumerate(s):
            if char in char_pos_record:
                res = max(res, i - left)
                left = max(left, char_pos_record[char] + 1)
            char_pos_record[char] = i

        return max(res, s_len - left)


print(Solution().lengthOfLongestSubstring('abbbbbb'))
