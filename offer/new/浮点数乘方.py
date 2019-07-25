class Solution:
    def Power(self, base, exponent):
        curr = exponent
        if exponent < 0:
            curr = -curr
        if exponent == 0:
            return 1
        res = 1
        while curr != 0:
            if (curr & 1) == 1:
                res *= base
            base *= base
            curr = curr >> 1
        if exponent > 0:
            return res
        else:
            return 1 / res


if __name__ == '__main__':
    print(Solution().Power(2, -3))