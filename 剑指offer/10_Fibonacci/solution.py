# // 面试题10：斐波那契数列
# // 题目：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。


def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        n1 = 0
        n2 = 1
        for i in range(3, n + 1):
            n1, n2 = n2, n1 + n2
        return n2


if __name__ == "__main__":
    a = 1
    b = 2
    a, b = b, a+b
    print(a, b)