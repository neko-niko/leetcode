# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# 示例 2：
#
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []

#思路：回溯搞起来
from typing import *

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        s_len = len(s)
        dct = {}
        def helper(ptr):        #回溯
            if ptr in dct:
                return dct[ptr]
            res = []
            if ptr == s_len:
                return []
            for word in wordDict:
                word_len = len(word)
                if s[ptr: ptr+word_len] == word:
                    if ptr + word_len == s_len:
                        res.append([word])
                        continue
                    temp = helper(ptr+word_len)
                    # if not temp:
                    #     res.append([word])
                    # else:
                    for i in temp:
                        res.append([word] + i)
            dct[ptr] = res
            return res


        res = helper(0)
        return res

"catsandog"
print(Solution().wordBreak("catsandog",["cats","dog","sand","and","cat"]))

