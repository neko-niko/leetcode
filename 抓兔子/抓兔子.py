

def Solution(n, k, check_lst: list):
    dp = [[1 for i in n] if j == 0 else [0 for i in n] for j in k+1]

    dp[0][check_lst[0] - 1] = 0
    for i in range(k):
        for j in range(n):
            if dp[i][j] == 1:
                if j == 0:
                    dp[i + 1][j + 1] = 1
                if j == n - 1:
                    dp[i + 1][j - 1] = 1
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j - 1] = 1
        dp[i + 1][check_lst[i + 1] - 1] = 0

    flag = True
    for i in dp[k]:
        if i == 1:
            flag = False
            break
    return 'yes' if flag else 'no'

