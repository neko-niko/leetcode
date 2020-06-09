class Solution:
    def StrToInt(self, s):
        pass

    def scaninter(self, ptr, s):
        befor = ptr
        s_len = len(s)
        if s[ptr] <= '9' and s[ptr] >= '0' and ptr < s_len:
            ptr += 1
        if ptr > befor:
            return True
        else:
            return False

    