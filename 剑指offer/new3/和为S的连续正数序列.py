# 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum <= 2:
            return []
        ptr1 = 1
        ptr2 = 2
        result = []
        sum = 1
        while ptr2 <= tsum:
            # print(ptr1, ptr2, sum)
            if sum < tsum:
                sum += ptr2
                ptr2 += 1
            elif sum == tsum:
                result.append(list(range(ptr1, ptr2)))
                sum -= ptr1
                ptr1 += 1
            elif sum > tsum:
                sum = sum - ptr1
                ptr1 += 1
        return result

if __name__ == '__main__':
    Solution().FindContinuousSequence(3)