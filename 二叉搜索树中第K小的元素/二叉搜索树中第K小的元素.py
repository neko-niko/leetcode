class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        def tree_insort_gen(root: TreeNode):
            if root is not None:
                yield from tree_insort_gen(root.left)
                yield root.val
                yield from tree_insort_gen(root.right)
        target_gen = tree_insort_gen(root)

        for i in range(k):
            result = target_gen.__next__()
        return result

class Solution2:
    def kthSmallest(self, root: TreeNode, k: int):
        cot = 0
        result = 0
        def TreeInsort(node: TreeNode):
            nonlocal cot, result
            if node is not None:
                TreeInsort(node.left)
                cot += 1
                if cot == k:
                    result = node.val
                    return
                TreeInsort(node.right)
        TreeInsort(root)
        return result

