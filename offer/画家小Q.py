# # 画家小Q又开始他的艺术创作。小Q拿出了一块有NxM像素格的画板, 画板初始状态是空白的,用'X'表示。
# # 小Q有他独特的绘画技巧,每次小Q会选择一条斜线, 如果斜线的方向形如'/',即斜率为1,小Q会选择这条斜线中的一段格子,都涂画为蓝色,用'B'表示;如果对角线的方向形如'\',即斜率为-1,小Q会选择这条斜线中的一段格子,都涂画为黄色,用'Y'表示。
# # 如果一个格子既被蓝色涂画过又被黄色涂画过,那么这个格子就会变成绿色,用'G'表示。
# # 小Q已经有想画出的作品的样子, 请你帮他计算一下他最少需要多少次操作完成这幅画。
# 输入描述:
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含两个正整数N和M(1 <= N, M <= 50), 表示画板的长宽。
# 接下来的N行包含N个长度为M的字符串, 其中包含字符'B','Y','G','X',分别表示蓝色,黄色,绿色,空白。整个表示小Q要完成的作品。
#
# 输出描述:
# 输出一个正整数, 表示小Q最少需要多少次操作完成绘画。



def Solution(N, M, color):
    cot = 0
    for i in range(N):
        for j in range(M):
            if color[j][i] == 'b':
                cot += 1
                painting_B(j, i, M, N, color)
            elif color[j][i] == 'y':
                cot += 1
                painting_Y(j, i, M, N, color)
            elif color[j][i] == 'g':
                cot += 2
                painting_Y(j, i, M, N, color)
                painting_B(j, i, M, N, color)




def painting_Y(x, y, m, n, color):
    if x >= 0 and x < m and y >= 0 and y < n and (color[x][y] =='y' or color[x][y] == 'g'):
        if color[x][y] == 'y':
            color[x][y] = 'x'
        else:
            color[x][y] = 'b'

    painting_Y(x-1, y-1, m, n, color)
    painting_Y(x+1, y+1, m, m, color)

def painting_B(x, y, m, n, color):
    if x >= 0 and x < m and y >= 0 and y < n and (color[x][y] =='b' or color[x][y] == 'g'):
        if color[x][y] == 'b':
            color[x][y] = 'x'
        else:
            color[x][y] = 'y'
    painting_B(x+1, y-1, m, n, color)
    painting_B(x-1, y+1, m, n, color)
