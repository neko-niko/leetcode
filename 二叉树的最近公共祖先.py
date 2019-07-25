# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if root is None:
            return root
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None
from typing import Optional, Set, List, Dict

class Solution2:
    def lowestCommonAncestor(self, root: Optional[TreeNode],
                             p: Optional[TreeNode],
                             q: Optional[TreeNode]) -> Optional[TreeNode]:
        stack: List[Optional[TreeNode]] = [root]
        map_parent: Dict[Optional[TreeNode], Optional[TreeNode]] = {root: None}
        while p not in map_parent or q not in map_parent:
            node: Optional[TreeNode] = stack.pop()
            if node.left:
                map_parent[node.left] = node
                stack.append(node.left)
            if node.right:
                map_parent[node.right] = node
                stack.append(node.right)
        ancestors: Set[TreeNode] = set()
        while p:
            ancestors.add(p)
            p = map_parent[p]
        while q not in ancestors:
            q = map_parent[q]
        return q