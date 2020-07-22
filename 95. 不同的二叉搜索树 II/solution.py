from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from functools import lru_cache
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        @lru_cache(128)
        def deep(left, right) -> List[TreeNode]:
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]
            ret = []
            for i in range(left, right+1):
                left_node_list = deep(left, i-1)
                right_node_list = deep(i+1, right)
                for left_node in left_node_list:
                    for right_node in right_node_list:
                        node = TreeNode(i)
                        node.left = left_node
                        node.right = right_node
                        ret.append(node)
            return ret

        return deep(1, n)




print(Solution().generateTrees(3))
