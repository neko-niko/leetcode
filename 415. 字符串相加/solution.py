class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        int_dict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        num1, num2 = num1[::-1], num2[::-1]

        flag = False
        ret_list = []

        pos = 0
        while pos < len(num1) and pos < len(num2):
            cur1 = int_dict[num1[pos]]
            cur2 = int_dict[num2[pos]]
            cur = cur1 + cur2
            if flag:
                cur += 1

            if cur >= 10:
                flag = True
            else:
                flag = False
            ret_list.append(str(cur % 10))
            pos += 1

        remain_nums = num1 if pos < len(num1) else num2

        while pos < len(remain_nums):
            cur = int_dict[remain_nums[pos]]
            if flag:
                cur += 1

            if cur >= 10:
                flag = True
            else:
                flag = False

            ret_list.append(str(cur % 10))
            pos += 1

        if flag:
            ret_list.append('1')
        return ''.join(reversed(ret_list))


print(Solution().addStrings('99', '999'))
