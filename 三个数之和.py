# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。


class Solution:
    def threeSum(self, nums: list) -> list:
        nums_len = len(nums)
        if nums_len < 3:
            return []
        nums = sorted(nums)

        result = []
        index = 0
        while index < nums_len and nums[index] <= 0:
            target = nums[index]
            ptr1 = index + 1
            ptr2 = nums_len - 1
            while ptr1 < ptr2:
                if nums[ptr1] + nums[ptr2] == -target:
                    result.append([target, nums[ptr1], nums[ptr2]])
                    while ptr1 < ptr2 and nums[ptr2-1] == nums[ptr2]:
                        ptr2 -= 1
                    while ptr1 < ptr2 and nums[ptr1+1] == nums[ptr1]:
                        ptr1 += 1
                    ptr1 += 1
                elif nums[ptr1] + nums[ptr2] > -target:
                    ptr2 -= 1
                else:
                    ptr1 += 1
            while index < nums_len-1 and nums[index+1] == nums[index]:
                index += 1
            index += 1
        return result


if __name__ == '__main__':
    print(Solution().threeSum([0, 0, 0]))


