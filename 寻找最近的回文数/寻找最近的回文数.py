# 给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。
#
# “最近的”定义为两个整数差的绝对值最小。
#
# 示例 1:
#
# 输入: "123"
# 输出: "121"




class Solution:
    def nearestPalindromic(self, n: str) -> str:
        str_len = len(n)
        mid = str_len // 2
        left_str = n[: str_len - mid]
        # mid_chat = n[mid]
        if str_len == 1:
            return str(int(n) - 1)

        candidate_lst = []
        x1 = int(left_str + ''.join(reversed(left_str))[1: ])
        candidate_lst.append(x1)
        x2 = int(left_str  + ''.join(reversed(left_str)))
        candidate_lst.append(x2)
        x3 = int(str(int(left_str) - 1) + ''.join(reversed(str(int(left_str) - 1)))[1: ])
        candidate_lst.append(x3)
        x4 = int(str(int(left_str) - 1) +  ''.join(reversed(str(int(left_str) - 1))))
        candidate_lst.append(x4)
        x5 = int(str(int(left_str) + 1) + ''.join(reversed(str(int(left_str) + 1)))[1: ])
        x6 = int(str(int(left_str) + 1) +  ''.join(reversed(str(int(left_str) + 1))))
        candidate_lst.append(x5)
        candidate_lst.append(x6)

        x7 = (10 ** (str_len-1) -1)
        x8 = (10 ** (str_len) + 1)
        candidate_lst.append(x7)
        candidate_lst.append(x8)

        filter_lst = []
        for i in candidate_lst:
            if i == int(n):continue
            filter_lst.append(i)
        res = -1
        num = int(n)
        for i in filter_lst:
            if abs(num - res) > abs(num - i): res = i
            if abs(num-res) == abs(num - i):
                if i < res:
                    res = i
        return str(res)




print(Solution().nearestPalindromic('1283'))
