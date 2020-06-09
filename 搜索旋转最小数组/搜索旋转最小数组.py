# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。

class Solution:
    def search(self, nums: list, target: int) -> int:
        lst_len = len(nums)
        if lst_len == 0:
            return -1
        if lst_len == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        ptr1, ptr2 = 0, lst_len - 1
        if nums[ptr1] < nums[ptr2]:
            return self.dichotomy_get_target(nums, ptr1, ptr2, target)
        else:
            demarcation_point = self.dichotomy_get_point(nums, ptr1, ptr2)        #分界点
            if demarcation_point is None:
                if target == nums[0]:
                    return 0
                else:
                    return -1
            else:
                left = self.dichotomy_get_target(nums, 0, demarcation_point, target)
                if left != -1:
                    return left
                return self.dichotomy_get_target(nums, demarcation_point + 1, lst_len - 1, target)



        # print(ptr1, ptr2, nums[ptr1], nums[ptr2])


    def dichotomy_get_point(self, lst: list, start, end):       #二分获得分界点
        if end - start == 1 and lst[start] > lst[end]:
            return start
        elif end - start == 1 and lst[start] == lst[end]:
            return None
        elif end - start == 1:
            return None
        else:
            midd = (end + start) // 2
            if lst[midd] > lst[start]:
                return self.dichotomy_get_point(lst, midd, end)
            elif lst[midd] < lst[start]:
                return self.dichotomy_get_point(lst, start, midd)
            else:
                left = self.dichotomy_get_point(lst, start, midd)
                if left is not None:
                    return left
                right = self.dichotomy_get_point(lst, midd, end)
                if right is not None:
                    return right
                else:
                    return None
    def dichotomy_get_target(self, lst: list, start, end, target):
        if end - start == 1 or end == start:
            if lst[end] != target and lst[start] != target:
                return -1
            else:
                return end if lst[end] == target else start
        else:
            midd = (start + end) // 2
            if lst[midd] > target:
                return self.dichotomy_get_target(lst, start, midd, target)
            if lst[midd] < target:
                return self.dichotomy_get_target(lst, midd, end, target)
            else:
                return midd





if __name__ == '__main__':
    print(Solution().search([1, 2, 3, 4, 5], 4))