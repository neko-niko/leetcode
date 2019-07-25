# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def dichotomy(strs: list, midd):
            target = strs[0][: midd]
            return all(map(lambda s: s[: midd] == target, strs))
        if not strs:
            return ''
        end = min(map(len, strs))
        start = 0

        while start <= end:
            midd = (start + end) // 2
            if dichotomy(strs, midd):
                start = midd + 1
            else:
                end = midd - 1
        return strs[0][0: (start + end) // 2]


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))