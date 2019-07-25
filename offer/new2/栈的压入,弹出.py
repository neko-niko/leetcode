# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) == 0 or len(popV) != len(pushV):
            return False
        stack = []
        ptr = 0
        for i in pushV:
            if popV[ptr] == i:
                ptr += 1
            else:
                stack.append(i)
        popV = list(reversed(popV[ptr: ]))
        print(popV, stack)
        return popV == stack



if __name__ == '__main__':
    Solution().IsPopOrder([1,2,3,4,5],[4,5,3,2,1])