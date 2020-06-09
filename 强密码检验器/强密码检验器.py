class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        upper_cot = 0
        lower_cot = 0
        repeat_cot = 0
        num_cot = 0
        s_len = len(s)
        pre = 887
        temp_cot = 0
        add_cot = 0
        for i in s:
            if i == pre:
                temp_cot += 1
                if temp_cot > 3:
                   add_cot = (temp_cot-1) // 2
            if i.islower():
                lower_cot += 1
                continue
            if i.isnumeric():
                num_cot += 1
                continue
            if i.isupper():
                upper_cot += 1
                continue

