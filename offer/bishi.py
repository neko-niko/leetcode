import sys


def Solution(lst: list, target: int):
    if len(lst) == 2:
        result = 0 if lst[0] == target else (len(lst) - 1 if lst[-1] == target else -1)
        return result

    midd = len(lst) // 2

    if lst[midd] > target:
        return midd + Solution(lst[0: midd], target)
    elif lst[midd] < target:
        return Solution(lst[midd + 1:], target)
    else:
        return midd
class test(object):

    test1 =