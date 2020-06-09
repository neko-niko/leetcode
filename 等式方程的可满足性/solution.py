from typing import List


class UnionFind:
    def __init__(self):
        self.root_store = {}

    def find(self, left):
        if left in self.root_store and self.root_store[left] != left:
            return self.find(self.root_store[left])

        return left

    def union(self, left, right):
        self.root_store[self.find(left)] = self.find(right)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        uf = UnionFind()

        for expression in equations:
            if expression[1] == "=":
                uf.union(expression[0], expression[3])
        for expression in equations:
            if expression[1] == "!":
                if uf.find(expression[0]) == uf.find(expression[3]):
                    return False

        return True


print(Solution().equationsPossible(["a==b","b!=a"]))