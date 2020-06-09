# // 面试题4：二维数组中的查找
# // 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
# // 照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
# // 整数，判断数组中是否含有该整数。

def Find(numbers, k):
    rows = len(numbers)
    if rows < 1:
        return False

    cols = len(numbers[rows - 1])

    if cols < 1:
        return False
    row_start = 0
    col_start = cols - 1
    while col_start >= 0 and row_start <= rows:
        if numbers[row_start][col_start] == k:
            return (row_start, col_start)
        elif numbers[row_start][col_start] >= k:
            col_start -= 1
        else:
            row_start += 1

