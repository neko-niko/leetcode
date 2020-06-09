# // 面试题11：旋转数组的最小数字
# // 题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# // 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组
# // {3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1。

def MinInOrder(numbers):
    j = len(numbers) - 1
    i = 0
    middle = 0

    while numbers[i] >= numbers[j]:
        if j - i == 1:
            middle = j
            break

        if numbers[i] == numbers[j] and numbers[middle] == numbers[i]:
            while i < j:
                if numbers[i + 1] >= numbers[i]:
                    i += 1
                else:
                    return numbers[i + 1]

        middle = (i + j) >> 1

        if numbers[middle] <= numbers[j]:
            j = middle

        else:
            i = middle

    return numbers[middle]
