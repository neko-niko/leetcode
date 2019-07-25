# n 个物品，它们有各自的重量和价值，现有给定容量的背包，如何让背包里装入的物品具有最大的价值总和？

def solution(n, val_lst, weight_lst, bp_size):

    if len(val_lst) != len(weight_lst) or n != len(val_lst):
        return
    else:
        val_lst.insert(0, 0)
        weight_lst.insert(0, 0)
        matrix = [[0 for _ in range(bp_size+1)] for i in range(n+1)]
        i = 1
        while i <= n:
            j = 1
            while j <= bp_size:
                if j < weight_lst[i]:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-weight_lst[i]] + val_lst[i])
                j += 1
            i += 1
        return matrix[n][bp_size]
