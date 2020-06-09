class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.rstrip().strip()
        s = [i for i in s]
        isnumber = self.number(s)
        try:
            if s[0] == '.':
                del s[0]
                isnumber = self.unsig_number(s) or isnumber     #短路运算注意
        except IndexError:
            pass
        try:
            if s[0] == 'e' or s[0] == 'E':
                del s[0]
                isnumber = isnumber and self.number(s)
        except IndexError:
            pass
        try:
            test = s[0]
            return False
        except IndexError:
            return isnumber



    def number(self, s: list) -> bool:
        try:
            if s[0] == '+' or s[0] == '-':
                del s[0]
                return self.unsig_number(s)
            else:
                return self.unsig_number(s)
        except:
            return False
    def unsig_number(self, s: list) -> bool:
        cot = 0
        while len(s) != 0 and s[0] <= '9' and s[0] >= '0':
            del s[0]
            cot += 1
        return cot != 0



if __name__ == '__main__':
    print(Solution().isNumber('0.8'))