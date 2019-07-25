# // 面试题8：二叉树的下一个结点
# // 题目：给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？
# // 树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。
from Utilities.BinaryTree import *

def get_next(pNode):
    if isinstance(pNode, BinartTreeNode) != True:
        return False

    if pNode.right != None:
        pNext = pNode.right
        while pNext.left != None:
            pNext = pNext.left

    elif pNode.parent != None:
        pCurrent, pNext = pNode, pNode.parent
        while pNext.right == pCurrent and pNext.parent != None:
            pCurrent, pNext = pNext, pNext.parent
    else:
        return False
    return pNext