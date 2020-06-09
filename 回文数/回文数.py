# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            t = 1e13
            while t > x:
                t = t / 10
            while x and x >= 10:

                temp1 = x % 10
                temp2 = x // t
                print(x, t, temp1, temp2)

                if temp1 != temp2:
                    print(1, temp1, temp2)
                    return False
                x = x % t

                x = x // 10
                cot = 0
                while t > x:
                    t = t / 10
                    cot += 1
                if cot == 2:
                    continue
                else:
                    cot = cot - 2
                    for i in range(cot):
                        if x % 10 == 0:
                            x = x // 10
                            t = t / 10
                        else:
                            print(2)
                            return False
            return True

print(Solution().isPalindrome(1000110001))