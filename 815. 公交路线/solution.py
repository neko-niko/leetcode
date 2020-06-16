from typing import List
from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        graph = defaultdict(set)

        routes = list(map(set, routes))
        for idx, route1 in enumerate(routes):
            for idx2 in range(idx+1, len(routes)):
                if any(i for i in routes[idx2] if i in route1):
                    graph[idx].add(idx2)
                    graph[idx2].add(idx)


        source = set()
        target = set()
        for idx, route in enumerate(routes):
            if S in route:
                source.add(idx)
            if T in route:
                target.add(idx)

        queue = [(idx, 1) for idx in source]
        for idx, deep in queue:
            if idx in target:
                return deep

            reachable_route = graph[idx]
            for idx2 in reachable_route:
                if idx2 not in source:
                    queue.append((idx2, deep+1))
                    source.add(idx2)

        return -1

        # for idx in range(len(routes)):
        #     route = set(routes[idx])
        #     if S in route:
        #         queue.add(idx)
        #         invalid_idx.add(idx)
        #
        #
        # step = 0
        #
        # while True:
        #     temp_queue = set()
        #
        #     step += 1
        #
        #     while queue:
        #         route = set(routes[queue.pop()])
        #         if T in route:
        #             return step
        #
        #         for node in route:
        #             for idx in range(len(routes)):
        #                 if idx not in invalid_idx and node in routes[idx]:
        #                     temp_queue.add(idx)
        #                     invalid_idx.add(idx)
        #     if not temp_queue:
        #         break
        #
        #     queue = temp_queue
        #
        # return -1

routes = [[1,2,7],[3,6,7]]
S = 1
T = 6

print(Solution().numBusesToDestination(routes, S, T))