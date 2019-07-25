class Solution:
    # s字符串
    def isNumeric(self, s: list):
        s = list(s)
        isnum = self.isInter(s)
        if s[0] == '.':
            s.remove(0)
            isnum = isnum or self.isunInter(s)
        if s[0] == 'e' or s[0] == 'E':
            s.remove(0)
            isnum = isnum and self.isInter(s)
        return len(s) == 0 and isnum

    def isunInter(self, s: list):
        cot = 0
        while len(s) > 0 and s[0] >= '0' and s[0] <= '9':
            s.remove(0)
            cot += 1
        return cot != 0

    def isInter(self, s):
        if s[0] in ('+', '-'):
            s.remove(0)
            return self.isunInter(s)
        else:
            return self.isunInter(s)

