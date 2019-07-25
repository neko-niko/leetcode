# 把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。


def Solution(String):
    str_len = len(String)
    String = list(String)
    if str_len == 0:
        return
    i = 0
    j = str_len - 1
    while String[i] >= 'a' and String[i] <= 'z' and i < str_len:
        i += 1
    while String[j] >= 'A' and String[j] <= 'Z' and j >= 0:
        j -= 1

    while i < j:
        String[i], String[j] = String[j], String[i]
        while String[i] >= 'a' and String[i] <= 'z' and i < str_len:
            i += 1
        while String[j] >= 'A' and String[j] <= 'Z' and j >= 0:
            j -= 1
    return ''.join(String)

if __name__ == '__main__':
    import sys
    while True:
        strs = sys.stdin.readline().strip()
        if strs == '':
            break
        else:
            print Solution(strs)