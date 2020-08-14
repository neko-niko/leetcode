class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {'(': ')', '[': ']', '{': '}'}
        if not s:
            return True
        for i in s:
            if i in dct:
                stack.append(i)
            else:
                if not stack:
                    return False

                if i == dct[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return not stack
