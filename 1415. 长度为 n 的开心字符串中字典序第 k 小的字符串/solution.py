class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if n <= 0:
            return ""

        def get_next_letter(letter: str) -> tuple:
            if letter == "a":
                return "b", "c"
            if letter == "b":
                return "a", "c"
            if letter == "c":
                return "a", "b"

            raise Exception("letter error")

        res = []
        def solve(happy_str: str):
            if len(happy_str) == n:
                res.append(happy_str)
                return

            for next_str in get_next_letter(happy_str[-1]):
                solve(happy_str+next_str)

        for letter in ("a", "b", "c"):
            solve(letter)

        if k > len(res):
            return ""

        return res[k-1]

print(Solution().getHappyString(3, 9))
