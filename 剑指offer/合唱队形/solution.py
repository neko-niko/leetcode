#
# 合唱队形
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 合唱队的N名学生站成一排且从左到右编号为1到N，其中编号为i的学生身高为Hi。
# 现在将这些学生分成若干组（同一组的学生编号连续），并让每组学生从左到右按身高从低到高进行排列，使得最后所有学生同样满足从左到右身高从低到高（中间位置可以等高），那么最多能将这些学生分成多少组？
#

# 4
# 2 1 3 2
# 样例输出
# 2
#
# 提示
# 补充样例
# 输入样例2
# 10
# 69079936 236011312 77957850 653604087 443890802 277126428 755625552 768751840 993860213 882053548
# 输出样例2
# 6
#
# 此时分组为：【69079936】【236011312 77957850】【653604087 443890802 277126428】 【755625552】 【768751840】【 993860213 882053548】调整顺序后即可满足条件

def solution(lst):
    stack = []

    res = 0

    n = len(lst)

    if n == 0:
        return 0
    if n == 1:
        return 1

    stack.append(lst[0])

    i = 1

    while i < n:
        if lst[i] > stack[-1]:
            # temp = []
            if len(set(stack)) == 1:
                res += len(stack)
                # print(stack)
                stack = []
            else:
                res += 1
                temp = []
                while stack:
                    temp.append(stack.pop())
                # print(temp)
            stack.append(lst[i])
        else:
            stack.append(lst[i])
        i += 1


    if len(set(stack)) == 1:
        for i in stack:
            print([i])
        return res + len(stack)
    else:
        temp = []
        while stack:
            temp.append(stack.pop())
        print(temp)
        return res + 1

def solution2(lst):
    stack = []

    res = 0

    n = len(lst)

    if n == 0:
        return 0
    if n == 1:
        return 1

    stack.append(lst[0])

    i = 1

    while i < n:
        if lst[i] > stack[-1]:
            # temp = []
            if len(set(stack)) == 1:
                res += len(stack)
                print(stack)
                stack = []
            else:
                res += 1
                temp = []
                while stack:
                    temp.append(stack.pop())
                print(temp)
            stack.append(lst[i])
        else:
            stack.append(lst[i])
        i += 1


    if len(set(stack)) == 1:
        print(stack)
        return res + len(stack)
    else:
        temp = []
        while stack:
            temp.append(stack.pop())
        return res + 1

if __name__ == '__main__':
    # input()
    # lst = list(map(int, input().split(' ')))
    str1 = '1 3 1 2'
    lst = list(map(int, str1.split(' ')))

    print(solution2(lst))