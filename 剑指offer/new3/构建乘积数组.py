class Solution:
    def multiply(self, A):
        B = []
        B.append(1)
        for i in A:
            B.append(B[-1]*i)
        B.pop()

        temp = 1
        cot = -2
        for i in reversed(A):
            temp = temp*i
            B[cot] = B[cot]*temp
            cot -= 1
            if abs(cot) > len(A):
                break
        return B
    