# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
class Solution:
    def MoreThanHalfNum_Solution2(self, numbers):
        cot_dct = {}
        for i in numbers:
            cot_dct.setdefault(i, 0)
            cot_dct[i] += 1
        for k, v in cot_dct.items():
            if v >= len(numbers) / 2:

                print(len(numbers) / 2)
                print(v)
                return k
        return 0

    def MoreThanHalfNum_Solution(self, numbers):
        middle = len(numbers) >> 1
        index = self.quick_sort(numbers, 0, len(numbers) - 1)
        while index != middle:
            if index < middle:
                index = self.quick_sort(numbers, index+1, len(numbers) - 1)
            else:
                index = self.quick_sort(numbers, 0, index-1)
        result = numbers[index]
        cot = 0
        for i in numbers:
            if i == result:
                cot += 1
        print(cot)
        if cot > middle:
            return result
        else:
            return 0
    def MoreThanHalfNum_Solution3(self, numbers):
        cot = 1
        result = numbers[0]
        for i in numbers[1:]:
            if cot == 0:
                result = i
                cot = 1
            elif i != result:
                cot -= 1
            else:
                cot += 1
    def quick_sort(self, arr, start, end):
        jizhun = arr[start]
        arr[start], arr[end] = arr[end], arr[start]
        index = start
        for i in range(index, end):
            if arr[i] < jizhun:
                arr[index], arr[i] = arr[i], arr[index]
                index += 1
        arr[index], arr[end] = arr[end], arr[index]
        return index





if __name__ == '__main__':

    print(Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))
