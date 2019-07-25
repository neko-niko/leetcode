# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
import typing


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        sort_lst = []
        for i in range(k):
            sort_lst.append(nums[i])

        sort_lst.sort()
        for j in range(k, len(nums)):
            if nums[j] > sort_lst[0]:

                sort_lst[0] = nums[j]
                sort_lst.sort()

        return sort_lst[0]


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
