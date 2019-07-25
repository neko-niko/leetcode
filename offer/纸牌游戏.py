# 牛牛和羊羊正在玩一个纸牌游戏。这个游戏一共有n张纸牌, 第i张纸牌上写着数字ai。
# 牛牛和羊羊轮流抽牌, 牛牛先抽, 每次抽牌他们可以从纸牌堆中任意选择一张抽出, 直到纸牌被抽完。
# 他们的得分等于他们抽到的纸牌数字总和。
# 现在假设牛牛和羊羊都采用最优策略, 请你计算出游戏结束后牛牛得分减去羊羊得分等于多少。




def quick_sort_core(lst, start, stop):
    flag = lst[start]
    ptr1 = start + 1
    ptr2 = start + 1
    while ptr2 <= stop:
        if lst[ptr2] > flag:
            lst[ptr1], lst[ptr2] = lst[ptr2], lst[ptr1]
            ptr1 += 1
            ptr2 += 1
        else:
            ptr2 += 1
    lst[start], lst[ptr1-1] = lst[ptr1-1], lst[start]
    ptr1 = ptr1 - 1
    if ptr1 > start:
        quick_sort_core(lst, start, ptr1)
    if ptr1 < stop:
        quick_sort_core(lst, ptr1+1, stop)
    return lst


def quick_sort(lst: list):
    lst_len = len(lst)
    return quick_sort_core(lst, 0, lst_len-1)


def Solution(nums, card_lst):

    lst_len = len(card_lst)
    if nums != lst_len:
        return
    else:
        lst = quick_sort(card_lst)
        niunius = lst[0: lst_len: 2]
        yangyangs = lst[1: lst_len :2]
        return sum(niunius) - sum(yangyangs)

# print(Solution(3, [2, 7, 4]))

