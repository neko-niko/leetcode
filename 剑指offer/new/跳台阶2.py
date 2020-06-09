class Solution:
    def jumpFloorII(self, number):
        cot = 1
        sum = 1
        while cot < number:
            sum = sum << 1
        return sum
