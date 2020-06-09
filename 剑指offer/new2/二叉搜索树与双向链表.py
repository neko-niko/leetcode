# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
#中序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None

        self.Convert(pRootOfTree.left)

        left = pRootOfTree.left
        if left:
            while left.right:
                left = left.right
            left.right = pRootOfTree
            pRootOfTree.left = left

        self.Convert(pRootOfTree.right)

        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
            right.left = pRootOfTree
            pRootOfTree.right = right
        while pRootOfTree.left: pRootOfTree = pRootOfTree.left
        return pRootOfTree