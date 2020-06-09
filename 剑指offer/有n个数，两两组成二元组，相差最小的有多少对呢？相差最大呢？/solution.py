# 6
# 45 12 45 32 5 6


def Sulotion(lst: list):
    max_cot = 0
    min_cot = 0
    max = -1
    min = 1e9
    lst_len = len(lst)
    i = 0
    while i < lst_len:
        j = i + 1
        while j < lst_len:
            sub = abs(lst[i] - lst[j])
            if sub == min:
                min_cot += 1
            elif sub < min:
                min_cot = 1
                min = sub
            else:
                pass

            if sub == max:
                max_cot += 1
            elif sub > max:
                max_cot = 1
                max = sub
            else:
                pass
            j += 1
        i += 1
    return (min_cot, max_cot)

print(Sulotion([45 ,12 ,45 ,32 ,5 ,6]))