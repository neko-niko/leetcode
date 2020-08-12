# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:

        filter_set = {}

        def deep(node: Node) -> Node:
            if not node:
                return node
            if node.val in filter_set:
                return filter_set[node.val]

            tmp = Node(node.val, [])
            filter_set[node.val] = tmp
            for n in node.neighbors:
                tmp.neighbors.append(deep(n))

            return tmp

        return deep(node)
