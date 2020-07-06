from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if not s1:
            return True
        if not s2:
            return False

        char_cot = Counter(s1)
        char_cot_c = Counter(s2[:len(s1)])
        def compare_dict(d1: dict, d2: dict):
            for k in d1.keys():
                if k in d2 and d2[k] == d1[k]:
                    continue
                return False
            return True

        for idx in range(len(s1), len(s2)):
            if compare_dict(char_cot, char_cot_c):
                return True
            char_cot_c[s2[idx]] += 1
            char_cot_c[s2[idx-len(s1)]] -= 1

        return compare_dict(char_cot, char_cot_c)




print(Solution().checkInclusion("adc", "dcda"))
