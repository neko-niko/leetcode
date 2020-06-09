# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        if len1 == 0 or len2 == 0:
            return ''
        ord_0 = ord('0')
        mul_lst = [0 for i in range(len1 + len2)]
        for i in reversed(range(0, len1)):
            for j in reversed(range(0, len2)):
                temp = (ord(num1[i]) - ord_0) * (ord(num2[j]) - ord_0)
                temp += (mul_lst[i+j+1] // 10)
                mul_lst[i+j+1] = mul_lst[i+j+1] % 10
                mul_lst[i+j] = mul_lst[i+j] + temp
        result = ''.join(map(lambda x: str(x), mul_lst[: -1])).lstrip('0')
        return '0' if result == '' else result

if __name__ == '__main__':
    print(Solution().multiply('5', '408'))