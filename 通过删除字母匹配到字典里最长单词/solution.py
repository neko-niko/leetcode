from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        if len(s) == 0:
            return ""

        d.sort(key=lambda key: (-len(key), key))

        def isSubStr(s: str, target: str) -> bool:
            if len(target) == 0:
                return True

            s_index = target_index = 0
            s_len, target_len = len(s), len(target)

            while True:

                if s[s_index] == target[target_index]:
                    s_index += 1
                    target_index += 1
                else:
                    s_index += 1

                if target_index == target_len:
                    return True

                if (s_len - s_index) < (target_len - target_index):
                    return False
        return next((sub_str for sub_str in d if isSubStr(s, sub_str)), "")

print(Solution().findLongestWord("bab", ["ba", "ab", "a", "b"]))
