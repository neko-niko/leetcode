
import sys

def solution(string: str):
    n = len(string)
    # print(n)
    res = 0
    i = 0
    flag = False
    if n == 0:
        return 0

    if n == 1:
        if string[0].isupper():
            return 2
        else:
            return 1


    while i < n:

        if not flag and string[i].islower():
            i += 1
            continue
        elif flag and string[i].isupper():
            i += 1
            continue
        elif not flag and string[i].isupper():
            if i + 1 < n:
                if string[i+1].isupper():
                    flag = True
                    # res += 1
            res += 1
            i += 1
        else:
            if i + 1 < n:
                if string[i+1].islower():
                    flag = False
            res += 1
            i += 1
    return res + n

    #     if not flag and string[i].isupper():
    #         if i + 1 < n and string[i+1].isupper():
    #             flag = True
    #         res += 1
    #     elif flag and string[i].islower():
    #         if i + 1 < n and string[i+1].islower():
    #             flag = False
    #         res += 1
    #     else:
    #         pass
    #
    # i += 1




if __name__ == '__main__':
    input()
    string = input().strip()

    print(solution(string))