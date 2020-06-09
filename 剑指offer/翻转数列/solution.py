# 小Q定义了一种数列称为翻转数列:
# 给定整数n和m, 满足n能被2m整除。对于一串连续递增整数数列1, 2, 3, 4..., 每隔m个符号翻转一次, 最初符号为'-';。
# 例如n = 8, m = 2, 数列就是: -1, -2, +3, +4, -5, -6, +7, +8.
# 而n = 4, m = 1, 数列就是: -1, +2, -3, + 4.
# 小Q现在希望你能帮他算算前n项和为多少。


def Solution(n, m):
    if n % (2*m) != 0:
        return False

    else:
        one_sum = m
        one_sum = m * one_sum
        total = one_sum * (n // (2*m))
        return total


print(Solution(4, 1))