from typing import List, Dict
from collections import defaultdict


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

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        return self.accountsMergeUF(accounts)

    def accountsMergeUF(self, accounts: List[List[str]]) -> List[List[str]]:

        unionFind = UnionFind()

        lookup = {}
        for index, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email in lookup:
                    unionFind.union(index, lookup[email])
                else:
                    lookup[email] = index

        res_set = defaultdict(set)
        for i in range(len(accounts)):
            root = unionFind.find(i)
            res_set[root].update(set(accounts[i][1:]))

        res = []
        for index, emails in res_set.items():
            res.append([accounts[index][0], *sorted(emails)])

        return res

    def accountsMergeSet(self, accounts: List[List[str]]) -> List[List[str]]:
        lookup_dict: Dict[List] = defaultdict(list)

        for account in accounts:
            name = account[0]
            emails = set(account[1:])

            lookup_dict[name].append(emails)

            for e in lookup_dict[name][:-1]:
                if e & emails:
                    lookup_dict[name].remove(e)
                    lookup_dict[name][-1].update(e)

        res = []
        for name, emails in lookup_dict.items():
            for e in emails:
                res.append([name, *sorted(e)])

        return res

    def accountsMergeDfs(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            email = account[1:]

            for e in email:
                email_to_name[e] = name
                graph[e].add(email[0])
                graph[email[0]].add(e)

        visited = set()
        res = []

        def dfs(e):
            new_list.append(e)
            for t in graph[e]:
                if t not in visited:
                    visited.add(t)
                    dfs(t)

        for e in graph:
            if e not in visited:
                visited.add(e)
                new_list = []
                dfs(e)
                res.append([email_to_name[e]] + sorted(new_list))
        return res
