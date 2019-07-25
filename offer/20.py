def scanUnsignedInterger(string, i):
    k = i[0]
    try:
        while string[i[0]] >= '0' and string[i[0]] <= '9':
            i[0] += 1
    except IndexError:
        pass
    return i[0] > k

def scanInterger(string, i):
    if string[i[0]] == '+' or string[i[0]] == '-':
        i[0] += 1

    return scanUnsignedInterger(string, i)

def isNumber(string):
    ptr = [0]
    lable = scanInterger(string, ptr)
    try:
        if string[ptr[0]] == '.':
            ptr[0] += 1
            # scanUnsignedInterger(string, ptr)
            lable = scanUnsignedInterger(string, ptr) or lable      #注意短路运算
        if string[ptr[0]] == 'e' or string[ptr[0]] == 'E':
            ptr[0] += 1
            lable = lable and scanInterger(string, ptr)
    except IndexError:
        pass
    return lable and ptr[0] == len(string)


if __name__ == "__main__":
    from unicodedata import normalize

    print(isNumber("1.1E"))