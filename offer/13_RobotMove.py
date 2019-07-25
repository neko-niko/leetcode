# // 面试题13：机器人的运动范围
# // 题目：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它
# // 每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和
# // 大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。
# // 但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

def check(rows, row, cols, col, k, visted):
    sum = 0
    while row % 10 != 0:
        sum += row % 10
        row = row % 10

    while col % 10 != 0:
        sum += col % 10
        col = col % 10
    if (sum <= k and col < cols and row < rows and row >= 0 and col >= 0 and visted[row][col] == 0):
        return True
    else:
        return False



def MoveCount(rows, row, cols, col, k, visted):
    visted[row][col] = 1
    count = 0
    if check(rows, row, cols, col, k, visted):
        count = 1 + MoveCount(rows, row - 1, cols, col, k, visted) + \
                MoveCount(rows, row + 1, cols, col, k, visted) + \
                MoveCount(rows, row, cols, col + 1, k, visted) + \
                MoveCount(rows, row, cols, col - 1, k, visted)

    return count
