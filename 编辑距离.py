# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2:
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == '':
            word1 = ' '
        if word2 == '':
            word2 = ' '
        str1_len = len(word1)
        str2_len = len(word2)

        matrix = [[0 for _ in range(str1_len+1)] for i in range(str2_len+1)]
        for i in range(str1_len):
            matrix[0][i] = i
        for i in range(str2_len):
            matrix[i][0] = i

        for i in range(1, str2_len+1):
            for j in range(1, str1_len+1):
                if word1[j-1] == word2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
        print(matrix)
        return matrix[str2_len][str1_len]


    def solution(self, word1: str, word2: str) -> int:
        if word1 == '':
            return len(word2)
        if word2 == '':
            return len(word1)
        matrix = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        for i in range(len(word1)):
            matrix[0][i] = i

        for j in range(len(word2)):
            matrix[j][0] = j

        for j in range(1, len(word1)+1):
            for i in range(1, len(word2)+1):
                if word1[j-1] == word2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1
        



print(Solution().minDistance("distance", "springbok"))