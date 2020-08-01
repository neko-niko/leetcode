import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        left, right = - (1 << 31), 1 << 31
        heapq_list = [(vec[0], vec, 0) for i, vec in enumerate(nums)]
        heapq.heapify(heapq_list)
        maxVal = max(x[0] for x in heapq_list)

        while True:
            minVal, vec, pos = heapq.heappop(heapq_list)
            if maxVal - minVal < right - left:
                right, left = maxVal, minVal

            if pos == len(vec) - 1:
                break

            pos += 1
            curVal = vec[pos]
            if curVal > maxVal:
                maxVal = curVal
            heapq.heappush(heapq_list, (curVal, vec, pos))


        return [left, right]


print(Solution().smallestRange([[11,38,83,84,84,85,88,89,89,92],[28,61,89],[52,77,79,80,81],[21,25,26,26,26,27],[9,83,85,90],[84,85,87],[26,68,70,71],[36,40,41,42,45],[-34,21],[-28,-28,-23,1,13,21,28,37,37,38],[-74,1,2,22,33,35,43,45],[54,96,98,98,99],[43,54,60,65,71,75],[43,46],[50,50,58,67,69],[7,14,15],[78,80,89,89,90],[35,47,63,69,77,92,94]]))
