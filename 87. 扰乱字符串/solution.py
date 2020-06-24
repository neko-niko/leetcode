class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len != s2_len:
            return False

        dp = [[[False for _ in range(s1_len + 1)] for _ in range(s1_len)] for _ in
              range(s1_len)]  # dp[i][j][n]表示从s1的i位置后的n个字符串和从s2的j位置后的n个字符串是否相等

        for i in range(s1_len):
            for j in range(s1_len):
                dp[i][j][1] = s1[i] == s2[j]


        for k_len in range(2, s1_len + 1):  # 要对比的长度从2开始(1已经在上面的循环中判断过)
            for i in range(s1_len - k_len + 1):  # 每次从0开始对比
                for j in range(s1_len - k_len + 1):
                    for pos in range(1, k_len):  # 每次要对比的k_len中的位置
                        if dp[i][j][pos] and dp[i + pos][j + pos][k_len - pos]:  # 没有交换
                            dp[i][j][k_len] = True
                            break
                        if dp[i][j + k_len - pos][pos] and dp[i + pos][j][k_len - pos]:  # 交换过
                            dp[i][j][k_len] = True
                            break

        return dp[0][0][s1_len]


