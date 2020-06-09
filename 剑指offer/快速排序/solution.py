
def kspx(lst, start, end):
    if start >= end:
        return
    else:
        flag = lst[start]
        ptr1 = start + 1
        ptr2 = start + 1
        while ptr2 <= end:
            if (lst[ptr2] <= flag):
                lst[ptr2], lst[ptr1] = lst[ptr1], lst[ptr2]
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
        index = ptr1 - 1
        lst[index], lst[start] = lst[start], lst[index]

        if index > start:
            kspx(lst, start, index-1)
        if index < end:
            kspx(lst, index+1, end)


