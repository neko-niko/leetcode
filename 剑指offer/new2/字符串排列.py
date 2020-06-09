# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
class Solution:
    def Permutation(self, ss):
        if len(ss) <= 0:
            return []
        res = []
        self.help2(list(ss), res, 0)
        return sorted(list(set(res)))


    def help(self, ss, res, ss2):
        if ss == '':
            res.append(ss2)
        else:
            for i in range(len(ss)):
                self.help(ss[:i]+ss[i+1], res, ss2+ss[i])

    def help2(self, ss, res, ptr):
        if ptr == len(ss) - 1:
            res.append(ss)
        else:
            for i in range(ptr, len(ss)):
                ss[i], ss[ptr] = ss[ptr], ss[i]
                self.help2(ss, res, ptr+1)
                ss[ptr], ss[i] = ss[i], ss[ptr]
