# 小Q的父母要出差N天，走之前给小Q留下了M块巧克力。小Q决定每天吃的巧克力数量不少于前一天吃的一半，但是他又不想在父母回来之前的某一天没有巧克力吃，请问他第一天最多能吃多少块巧克力

def Sum(a1, q, n):
    return (a1 * (1 - pow(q, n))) / (1 - q)


def Solution(days, total):
    Max = -1
    for i in range(1, total+1):
        if Sum(i, 2, days) < total:
            continue
        elif Sum(i, 2, days) == total:
            Max = i
            break
        else:
            Max = i - 1
            break
    if Max < 0:
        return
    # print(Max)
    for i in range(days-1):
        Max = Max * 2

    return Max

print(Solution(2, 124))