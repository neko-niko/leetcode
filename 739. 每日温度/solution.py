from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        if len(T) == 1:
            return [0]

        res = [0 for _ in range(len(T))]
        stack = [0]
        for day in range(1, len(T)):
            while stack and T[stack[-1]] < T[day]:
                stack_top = stack.pop()
                res[stack_top] = day - stack_top
            stack.append(day)

        return res
