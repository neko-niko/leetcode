# 小Q有X首长度为A的不同的歌和Y首长度为B的不同的歌，现在小Q想用这些歌组成一个总长度正好为K的歌单，每首歌最多只能在歌单中出现一次，在不考虑歌单内歌曲的先后顺序的情况下，请问有多少种组成歌单的方法。
#
# 输入描述:
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含一个整数，表示歌单的总长度K(1<=K<=1000)。
# 接下来的一行包含四个正整数，分别表示歌的第一种长度A(A<=10)和数量X(X<=100)以及歌的第二种长度B(B<=10)和数量Y(Y<=100)。保证A不等于B。
#
# 输出描述:
# 输出一个整数,表示组成歌单的方法取模。因为答案可能会很大,输出对1000000007取模的结果。

def Solution(K, A, X, B, Y):
    if K == 0:
        print(1)
        return 1
    elif K < 0:
        return 0
    else:
        if X == 0:
            if K % B == 0 and K // B <= Y:
                print(2)
                return 1
            else:
                return 0
        if Y == 0:
            if K % A == 0 and K // A <= X:
                print(3)
                return 1
            else:
                return 0
        return Solution(K-A, A, X-1, B, Y) + Solution(K-Y, A, X, B, Y-1)

print(Solution(5, 2, 3, 3, 3))