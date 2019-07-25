# “student. a am I”
#两次翻转

class Solution:
    def ReverseSentence(self, s):
        s_len = len(s)
        s = list(s)
        i = 0
        j = s_len - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        i = 0

        for index, v in enumerate(s):
            if v == ' ':
                j = index - 1
                while i < j:
                    s[i], s[j] = s[j], s[i]
                    i += 1
                    j -= 1

                i = index + 1
            if index == s_len - 1:
                j = index
                while i < j:
                    s[i], s[j] = s[j], s[i]
                    i += 1
                    j -= 1

        return ''.join(s)