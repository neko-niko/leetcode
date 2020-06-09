# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) == 0:
            return []
        numbers = list(numbers)
        self.kspx(numbers, 0, len(numbers) - 1)
        numbers = map(lambda x: str(x), numbers)
        return ''.join(numbers)

    def kspx(self, lst, start, end):
        if start == end:
            return
        index = self.kspx_core(lst, start, end)
        print(index, start, end)
        if index > start:
            self.kspx(lst, start, index - 1)
        if index < end:
            self.kspx(lst, index + 1, end)

    def cmp(self, a, b):
        if str(a) + str(b) > str(b) + str(a):
            return 1
        elif str(a) + str(b) < str(b) + str(a):
            return -1
        else:
            return 0

    def kspx_core(self, lst, start, end):
        jizhun = lst[start]
        index = start + 1
        for i in range(index, end + 1):
            if self.cmp(lst[i], jizhun) >= 0:
                pass
            else:
                lst[index], lst[i] = lst[i], lst[index]
                index += 1
        lst[0], lst[index - 1] = lst[index - 1], lst[0]
        return index

Solution().PrintMinNumber([1,2,111])


