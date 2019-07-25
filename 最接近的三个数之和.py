# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums: list, target: int):
        lst_len = len(nums)
        if lst_len < 3:
            return None
        elif lst_len == 3:
            return sum(nums)
        else:
            nums = list(sorted(nums))
            result = 1e13
            ptr = 0
            while ptr < lst_len - 2:
                temp1 = ptr + 1
                temp2 = lst_len - 1
                ptr_num = nums[ptr]
                while temp1 < temp2:
                    temp_num = nums[temp2] + nums[temp1] + ptr_num
                    if temp_num == target:
                        return target
                    else:
                        if abs(temp_num - target) < abs(result - target):
                            result = temp_num
                        if temp_num > target:
                            temp2 -= 1
                        else:
                            temp1 += 1
                ptr += 1
            return result


class Solution2:
    def threeSumClosest(self, nums: list, target: int):
        lst_len = len(nums)
        if lst_len < 3:
            return None
        elif lst_len == 3:
            return sum(nums)
        else:
            nums = list(sorted(nums))
            result = []
            ptr = 0
            while ptr < lst_len - 2:
                temp1 = ptr + 1
                temp2 = lst_len - 1
                ptr_num = nums[ptr]
                if ptr_num + nums[temp1] + nums[temp1+1] > target:
                    result.append(ptr_num + nums[temp1] + nums[temp1+1])
                elif ptr_num + nums[temp2] + nums[temp2 - 1] < target:
                    result.append(ptr_num + nums[temp2] + nums[temp2 - 1])
                else:
                    while temp1 < temp2:
                        temp_num = nums[temp2] + nums[temp1] + ptr_num
                        result.append(temp_num)

                        if temp_num == target:
                            return target
                        else:
                            if temp_num > target:
                                temp2 -= 1
                            else:
                                temp1 += 1
                ptr += 1
            return list(sorted(result, key=lambda x: abs(x - target)))[0]
if __name__ == '__main__':
    print(Solution2().threeSumClosest([-1, 2, 1, -4], 1))