class Solution:
    def maxInWindows(self, num, size):
        result = []
        queue = []
        if size == 0 or size > len(num):
            return result
        for i in range(size):
            if queue and num[i] > num[queue[0]]:
                del queue[0]
            queue.insert(0, i)
        for i in range(size, len(num)):
            result.append(num[queue[-1]])
            while queue and num[i] >= num[queue[0]]:
                del queue[0]
            if queue and queue[-1] <= i - size:
                queue.pop()
            queue.insert(0, i)
        result.append(num[queue[-1]])
        return result

Solution().maxInWindows([2,3,4,2,6,2,5,1],3)