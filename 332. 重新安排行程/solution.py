from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []

        dct = defaultdict(list)
        for ticket in tickets:
            dct[ticket[0]].append(ticket[1])
            dct[ticket[0]].sort()
        if "JFK" not in dct:
            return []

        res = []

        def deep(start_point: str):
            end_point = dct[start_point]
            while end_point:
                next_point = end_point[0]
                end_point.remove(next_point)
                deep(next_point)
            res.append(start_point)

        deep("JFK")

        return res[::-1]


print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
