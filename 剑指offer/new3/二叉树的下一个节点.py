# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return None

        if pNode.right is not None:
            pNext = pNode.right
            while pNext.left is not None:
                pNext = pNext.left
            return pNext

        else:
            pPar = pNode.next
            if pPar is None:
                return None
            if pNode == pPar.left:
                pNext = pPar
                return pNext

            if pNode == pPar.right:
                pNode = pPar
                pPar = pPar.next
                while pPar is not None and pNode == pPar.right:
                    pNode = pPar
                    pPar = pPar.next
                pNext = pPar
                return pNext

