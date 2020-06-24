from abc import abstractclassmethod

class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for s in path.split("/"):
            res = {"": res, ".": res, "..": res[:-1]}.get(s, res + [s])

        return '/' + '/'.join(res)


# print(Solution().simplifyPath('/a/../../b/../c//.//'))


def test_func():
    pass

print(type(Solution.simplifyPath))

