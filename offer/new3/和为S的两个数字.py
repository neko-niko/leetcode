# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        lst_len = len(array)
        if lst_len <= 1:
            return None
        ptr1 = 0
        ptr2 = lst_len - 1
        while ptr1 < ptr2:
            if array[ptr1] + array[ptr2] == tsum:
                return [array[ptr1], array[ptr2]]
            elif array[ptr1] +array[ptr2] < tsum:
                ptr1 += 1
            else:
                ptr2 -= 1
        return None


Solution().FindNumbersWithSum([1,2,4,7,11,16],10)