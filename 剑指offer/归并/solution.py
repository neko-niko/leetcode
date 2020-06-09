
def gbpx(lst):
    if len(lst) <= 1:
        return lst
    else:
        left = gbpx(lst[0: len(lst) // 2])
        right = gbpx(lst[len(lst) // 2: ])
        return core(left, right)

def core(left, right):
    l = r = 0
    lst = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            lst.append(left[l])
            l += 1
        else:
            lst.append(right[r])
            r += 1

    lost = left[l: ] if l < len(left) else right[r: ]
    lst += lost
    return lst


def gbpx(lst):
    lst_len = len(lst)
    if lst_len <= 1:
        return lst
    else:
        left = gbpx(lst[0: lst_len // 2])
        right = gbpx(lst[lst_len // 2: ])
        l = r = 0
        left_len = len(left)
        right_len = len(right)
        result_lst = []
        while l <= left_len-1 and r <= right_len-1:
            if left[l] <= right[r]:
                result_lst.append(left[l])
                l += 1
            else:
                result_lst.append(right[r])
                r += 1
        last = left[l:] if r == right else right[r:]
        return result_lst + last