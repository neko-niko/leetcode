# // 面试题5：替换空格
# // 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，
# // 则输出“We%20are%20happy.”

def Replace(string, be_rep, to_rep):
    be_len = len(be_rep)
    to_len = len(to_rep)
    # if to_len >= be_rep:
    diff = to_len - be_len
    be_cot = 0
    for i in string:
        if i == be_rep:
            be_cot += 1
    old = len(string) - 1
    new = len(string) - 1 + diff * be_cot

    string += [' '] * diff * be_cot
    while new > 0:
        if string[old] != be_rep:
            string[new] = string[old]
            new -= 1
            old -= 1
        else:
            old -= 1
            for j in range(diff + 1):
                string[new] = to_rep[to_len - 1 - j]
                new -= 1
    return string

if __name__ == "__main__":
    str = 'asdfgcddff'
    lst = []
    for i in str:
        lst.append(i)

    str2 = Replace(lst, 'f', '测试')
    print(''.join(str2))