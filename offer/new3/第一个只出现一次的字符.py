# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

class Solution:
    def FirstNotRepeatingChar(self, s):
        cot_dct = {}
        for i in s:
            cot_dct.setdefault(i, 0)
            cot_dct[i] += 1
        i = 0
        while i < len(s):
            if cot_dct[s[i]] == 1:
                return i
            i += 1
        return -1
