# 利用相同的数异或为0的性质

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        tmp = 0
        for i in array:
            tmp = tmp ^ i
        cot = 0
        while tmp & 1 == 0:
            tmp = tmp >> 1
            cot += 1
        num1 = num2 = 0
        for i in array:
            if self.Bit(i, cot):
                num1 = num1 ^ i
            else:
                num2 = num2 ^ i
        return num1, num2


    def Bit(self, num, cot):
        for i in range(cot):
            num = num >> 1
        return num & 1 == 0