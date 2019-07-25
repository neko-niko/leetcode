from Utilities.BinaryTree import *


def ConvertNode(pRoot, lastNode):
    if pRoot == None:
        return None
    if pRoot.left != None:
        ConvertNode(pRoot.left, lastNode)
    pRoot.left = lastNode
    if lastNode != None:
        lastNode.right = pRoot
    lastNode = pRoot
    if pRoot.right != None:
        ConvertNode(pRoot, lastNode)