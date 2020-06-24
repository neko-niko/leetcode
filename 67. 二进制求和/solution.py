class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)

        ptr_a, ptr_b = len_a - 1, len_b - 1

        carry_flag = False
        res = []
        while ptr_a >= 0 and ptr_b >= 0:

            cur_a = a[ptr_a]
            cur_b = b[ptr_b]
            ptr_b -= 1
            ptr_a -= 1
            if carry_flag:
                if cur_a == '1' and cur_b == '1':
                    carry_flag = True
                    cur_res = '1'
                elif cur_a == '1' or cur_b == '1':
                    carry_flag = True
                    cur_res = '0'
                else:
                    carry_flag = False
                    cur_res = '1'
            else:
                if cur_a == '1' and cur_b == '1':
                    carry_flag = True
                    cur_res = '0'
                elif cur_a == '1' or cur_b == '1':
                    carry_flag = False
                    cur_res = '1'
                else:
                    carry_flag = False
                    cur_res = '0'
            res.append(cur_res)

        cur_num = a if len_a > len_b else b
        cur_ptr = ptr_a if ptr_a >= 0 else ptr_b

        while cur_ptr >= 0:
            cur_bit = cur_num[cur_ptr]
            cur_ptr -= 1
            if carry_flag:
                if cur_bit == '1':
                    res.append('0')
                    carry_flag = True
                else:
                    res.append('1')
                    carry_flag = False
            else:
                res.append(cur_bit)

        if carry_flag:
            res.append('1')

        return ''.join(reversed(res))


print(Solution().addBinary('1111', '1'))
