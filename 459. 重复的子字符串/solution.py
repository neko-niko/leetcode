class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (2 * s).find(s, 1) != len(s)
