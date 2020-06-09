# // 面试题3（二）：不修改数组找出重复的数字
# // 题目：在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至
# // 少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的
# // 数组。例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的
# // 输出是重复的数字2或者3。


def RangeCount(number, start, end):
    cot = 0
    for i in range(len(number)):
        if number[i] >= start and number[i] <= end:
            cot += 1

    return cot

def GetDuplication(number):
    length = len(number)
    start = 1
    end = length - 1
    while start <= end:
        middle = (start + end) >> 1
        cot = RangeCount(number, start, middle)
        if cot > (middle - start + 1):
            end = middle
        else:
            start = middle + 1
        if start == end:
            cot = RangeCount(number, start, end)
            if cot > 1:
                return start
            else:
                return None





if __name__ == "__main__":
    print(GetDuplication([1,2,3]))