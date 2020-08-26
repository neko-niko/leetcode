from typing import List
import time


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        number_to_letter: dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }


        res: List[str] = []

        def deep(pos: int, cur: str):
            if pos == len(digits):
                res.append(cur)
                return
            if digits[pos] not in number_to_letter:
                deep(pos + 1, cur)
            else:
                for i in number_to_letter[digits[pos]]:
                    deep(pos + 1, cur + i)

        deep(0, '')
        return res


Solution().letterCombinations('2222222222222')
