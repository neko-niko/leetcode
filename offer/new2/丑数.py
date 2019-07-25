# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        Ugly_lst = []
        Ugly_lst.append(1)
        ptr_1 = ptr_2 = ptr_3 = 0
        ptr = 0
        while ptr < index:
            while Ugly_lst[ptr_1] * 2 <= Ugly_lst[ptr]:
                ptr_1 += 1
            while Ugly_lst[ptr_2] * 3 <= Ugly_lst[ptr]:
                ptr_2 += 1
            while Ugly_lst[ptr_3] * 5 <= Ugly_lst[ptr]:
                ptr_3 += 1
            ptr += 1
            Ugly_lst.append(min(2*Ugly_lst[ptr_1], 3*Ugly_lst[ptr_2], 5*Ugly_lst[ptr_3]))
        return Ugly_lst[index-1]