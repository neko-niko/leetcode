class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):

        ptr1 = 0
        ptr2 = 0
        return self.matchCore(s, pattern, ptr1, ptr2)

    def matchCore(self, s, pattern, ptr1, ptr2):
        if ptr1 == len(s) and ptr2 == len(pattern):
            return True
        elif ptr1 != len(s) and ptr2 == len(pattern):
            return False
        else:
            if ptr2+1 < len(pattern) and pattern[ptr2+1] == '*':
                if ptr1 < len(s) and (pattern[ptr2] == '.' or pattern[ptr2] == s[ptr1]):
                    return (self.matchCore(s, pattern, ptr1+1, ptr2) or self.matchCore(s, pattern, ptr1+1, ptr2+2) or self.matchCore(s, pattern, ptr1, ptr2+2))
                else:
                    return self.matchCore(s, pattern, ptr1, ptr2+2)
            elif ptr1 < len(s) and (pattern[ptr2] == s[ptr1] or pattern[ptr2] == '.'):
                return self.matchCore(s, pattern, ptr1+1, ptr2+1)
            else:
                return False


Solution().match("aaa","ab*ac*a")