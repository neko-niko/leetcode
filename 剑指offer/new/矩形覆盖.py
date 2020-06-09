# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
class Solution:
    def rectCover(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            lst = [1, 1]
            [lst.append(lst[x-1] + lst[x-2]) for x in range(2, n+1)]
            return lst[-1]
