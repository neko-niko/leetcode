
def get_nextnums(string: str):
    string_lst = [i for i in string]
    result = [0 for i in range(len(string_lst))]
    # result[0] = -1
    k = 0
    for i in range(1, len(string_lst) - 1):
        if string_lst[i] == string_lst[k]:
            print(string_lst[i], string_lst[k], k)
            result[i + 1] = k + 1
            k += 1
        else:
            print(k)
            while k != 0:
                k = result[k]
                print(k)
                if string_lst[k] == string_lst[i]:
                    result[i + 1] = k
                    k += 1
            else:
                result[i + 1] = k
    return result



if __name__ == '__main__':
    print(get_nextnums('abcabcff'))