class Solution:
    def myAtoi(self, str1: str) -> int:
        str1 = str1.strip().rstrip()
        if str1 == '':
            return 0

        if str1[0] == '-' or str1[0] == '+':
            flag = str1[0]
            str1 = str1[1:]
            i = 0
            for j in str1:
                if j >= '0' and j <= '9':
                    i += 1
                    continue
                else:
                    break

            str1 = ''.join(reversed(str1[: i]))
            result = self.atoi_core(str1[: i])
            result = 0 - self.atoi_core(str1[: i]) if flag == '-' else result

        elif str1[0] >= '0' and str1[0] <= '9':
            i = 0
            for j in str1:
                if j >= '0' and j <= '9':
                    i += 1
                    continue
                else:
                    break

            str1 = ''.join(reversed(str1[: i]))
            result = self.atoi_core(str1)
        else:
            return 0

        flag = pow(2, 31)
        if result >= flag - 1:
            return flag - 1
        elif result <= -flag:
            return (-1 * flag)
        else:
            return result

    def atoi_core(self, str: str) -> int:
        if str == "":
            return 0
        if str[0] >= '0' and str[0] <= '9':
            return int(str[0]) + 10 * self.atoi_core(str[1:])
        else:
            return 0


class Solution2:
    def myAtoi(self, str1: str) -> int:
        str1 = str1.strip().rstrip()
        if str1 == '':
            return 0
        if str1[0] == '-' or str1[0] == '+':
            flag = str1[0]
            result = self.atoi_core(str1[1:])
            result = result if flag == '+' else -result

        elif str1[0] <= '9' and str1[0] >= '0':
            result = self.atoi_core(str1)
        else:
            return 0


        flag = pow(2, 31)
        if result >= flag - 1:
            return flag - 1
        elif result <= -flag:
            return (-1 * flag)
        else:
            return result
    def atoi_core(self, str1: str) -> int:
        i = 0
        for j in str1:
            if j <= '9' and j >= '0':
                i += 1
            else:
                break
        if i == 0:
            return 0
        return int(str1[0: i])






print(Solution().myAtoi("2147483648"))
