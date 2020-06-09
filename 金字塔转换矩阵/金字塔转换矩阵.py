# 现在，我们用一些方块来堆砌一个金字塔。 每个方块用仅包含一个字母的字符串表示，例如 “Z”。
#
# 使用三元组表示金字塔的堆砌规则如下：
#
# (A, B, C) 表示，“C”为顶层方块，方块“A”、“B”分别作为方块“C”下一层的的左、右子块。当且仅当(A, B, C)是被允许的三元组，我们才可以将其堆砌上。
#
# 初始时，给定金字塔的基层 bottom，用一个字符串表示。一个允许的三元组列表 allowed，每个三元组用一个长度为 3 的字符串表示。
#
# 如果可以由基层一直堆到塔尖返回true，否则返回false。

from typing import *
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        tar_dct = {}
        for i in allowed:
            tar_dct.setdefault(i[:2], [])
            tar_dct[i[:2]].append(i[2])

        def get_list(bottom, index, n, temp, res_lst):
            if index == n-1:
                res_lst.append(temp)
            else:
                for i in tar_dct[bottom[index: index+2]]:
                    get_list(bottom, index+1, n, temp+i, res_lst)


        def help(bottom):
            if len(bottom) == 1:
                return True
            else:
                for i in range(len(bottom) - 1):
                    if bottom[i: i+2] not in tar_dct:
                        return False

                next_strs = []
                get_list(bottom, 0, len(bottom), '', next_strs)
                for i in next_strs:
                    if help(i):
                        return True
                return False

        return help(bottom)
