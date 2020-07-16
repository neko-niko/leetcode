from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        target_list = [0 for _ in graph]

        def dfs(node, cur):
            nei = 1 if cur == 2 else 2
            if target_list[node] == cur:
                return True
            elif target_list[node] == nei:
                return False
            else:
                target_list[node] = cur
                for i in graph[node]:
                    if not dfs(i, nei):
                        return False
            return True

        for node, color in enumerate(target_list):
            if color == 0:
                res = dfs(node, 1)
                if not res:
                    return False

        return True


print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
