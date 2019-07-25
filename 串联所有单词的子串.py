# 给定一个字符串
# s
# 和一些长度相同的单词
# words。找出
# s
# 中恰好可以由
# words
# 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与
# words
# 中的单词完全匹配，中间不能有其他字符，但不需要考虑
# words
# 中单词串联的顺序。
#
#
#
# 示例
# 1：
#
# 输入：
# s = "barfoothefoobarman",
# words = ["foo", "bar"]
# 输出：[0, 9]
# 解释：
# 从索引
# 0
# 和
# 9
# 开始的子串分别是
# "barfoor"
# 和
# "foobar" 。
# 输出的顺序不重要, [9, 0]
# 也是有效答案。
# 示例
# 2：
#
# 输入：
# s = "wordgoodgoodgoodbestword",
# words = ["word", "good", "best", "word"]
# 输出：[]

from typing import *


class Solution:
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        word_len = len(words[0])
        all_len = word_len * len(words)
        result = []
        words = Counter(words)
        for i in range(0, len(s) - all_len + 1):
            sub_words = []
            for j in range(i, i + all_len, word_len):
                sub_words.append(s[j: j + word_len])
            if Counter(sub_words) == words:
                result.append(i)
        return result

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []

        word_len = len(words[0])
        all_len = word_len * len(words)
        result = []
        words = Counter(words)
        s_len = len(s)
        for i in range(word_len):
            left = right = i
            temp_cot = {}
            while left + all_len <= s_len:
                temp_word = s[right: right + word_len]
                right += word_len
                if temp_word not in words:
                    left = right
                    temp_cot.clear()
                else:
                    temp_cot.setdefault(temp_word, 0)
                    temp_cot[temp_word] += 1
                    while temp_cot[temp_word] > words[temp_word]:
                        temp_cot[s[left: left + word_len]] -= 1
                        left += word_len

                    if right - left == all_len:
                        result.append(left)
        return result

class Solution2:
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []
        lens = len(s)
        lenw = len(words[0])
        lenws = lenw * len(words)
        if lens < lenws:
            return []
        counter = {}
        for i in range(len(words)):
            if words[i] in counter:
                counter[words[i]] += 1
            else:
                counter[words[i]] = 1
        res = []
        for i in range(min(lenw, lens - lenws + 1)):
            s_pos = word_pos = i
            d = {}
            while s_pos + lenws <= lens:
                # 截取单词
                word = s[word_pos:word_pos + lenw]
                # 移动到下一个单词
                word_pos += lenw
                if word not in counter:
                    s_pos = word_pos
                    d.clear()
                else:
                    if word not in d:
                        d[word] = 1
                    else:
                        d[word] += 1
                    while d[word] > counter[word]:
                        d[s[s_pos:s_pos + lenw]] -= 1
                        s_pos += lenw
                    if word_pos - s_pos == lenws:
                        res.append(s_pos)
        return res


if __name__ == '__main__':
    print(Solution().findSubstring("barfoothefoobarman", ['bar', 'foo', 'the']))

    # print(test_dct)
