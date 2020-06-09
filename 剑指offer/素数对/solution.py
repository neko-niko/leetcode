# 给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
# 如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)）
import math

def Solution(num):
    cot = 0
    for i in range(1, (num // 2)+1):
        if Judge(i):
            if Judge(num-i):
                cot += 1
    return cot






def Judge(num):
    if num <= 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        else:
            continue
    return True

print(Solution(10000000))