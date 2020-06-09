class Solution:
    def FindGreatestSumOfSubArray(self, array):
        currsum = 0
        max_ = -1e9
        for i in array:
            if currsum <= 0:
                currsum = i
            else:
                currsum += i
            if currsum > max_:
                max_ = currsum
        return max_


print(Solution().FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))
