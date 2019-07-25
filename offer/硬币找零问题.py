
def Solution(arr: list, target):

    dp = [[0 for i in range(target)] for j in arr]

    for i in range(target + 1):
        if i == 0:
            dp[0][i] = 0
        else:
            if i % arr[0] == 0:
                dp[0][i] = i // arr[0]
            else:
                dp[0][i] = (1 << 31)
    for i in range(1, len(arr)):
        for j in range(target + 1):
            left = (1 << 31)
            if dp[i][j - arr[i]] != (1 << 31):
                left = 1 + dp[i][j - arr[i]]
            dp[i][j] = min(left, dp[i - 1][j])
