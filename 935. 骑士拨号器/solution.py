class Solution:
    def knightDialer(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [1] * 10       # 初始的dp矩阵, 同时也表示了n为1时的情况
        for _ in range(N - 1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):       # 遍历能到达所有情况, COUNT为第n步时, 到达此点的情况总和
                for j in moves[node]:       # 当前点能到达哪一个其余点
                    dp2[j] += count
                    dp2[j] %= MOD
            dp = dp2

        return sum(dp) % MOD


print(Solution().knightDialer(2))
