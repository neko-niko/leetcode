# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
class Solution:
    def jumpFloor(self, number):
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            lst = [1, 2]
            [lst.append(lst[x-1] + lst[x-2]) for x in range(2, number)]
            return lst[-1]