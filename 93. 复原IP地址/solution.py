from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def deep(tmp: str, s: str, dot_cot):
            if not s:
                return
            if dot_cot == 3:
                if s[0] == '0' and len(s) > 1:
                    return
                if self.isValid(s):
                    res.append(tmp+s)
            else:
                if s[0] == '0':
                    deep(tmp+'0.', s[1:], dot_cot+1)
                else:
                    for sub_len in range(min(3, len(s))):
                        if self.isValid(s[:1+sub_len]):
                            deep(tmp+s[:1+sub_len]+'.', s[1+sub_len:], dot_cot+1)
        deep("", s, 0)
        return res


    def isValid(self, s: str) -> bool:
        s_int = int(s)
        if s_int >= 0 and s_int <= 255:
            return True
        return False
