# // 面试题14：剪绳子
# // 题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
# // 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
# // 积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
# // 时得到最大的乘积18。

def maxProCutRope(length):
    if length < 2:
        return False
    if length < 3:
        return 1
    if length < 4:
        return 2
    if length < 5:
        return 4

    products = [0, 1, 2, 3, 4]
    for i in range(5, length + 1):
        max = 0
        for j in range(1, (length >> 1) + 1):
               product = products[j] * products[i - j]
               if product > max:
                   max = product

        products[i] = max
    return products[length]
