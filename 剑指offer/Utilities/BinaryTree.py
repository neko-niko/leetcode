import gc

class BinartTreeNode(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def CreateBinaryTreeNode(value,left = None, right = None):
    pNode = BinartTreeNode(value, left, right)
    return pNode

def ConnectTreeNodes(pParent, pleft, pright):
    if isinstance(pParent, BinartTreeNode) == False \
            or isinstance(pleft, BinartTreeNode) == False \
            or isinstance(pright, BinartTreeNode) == False:
        raise ValueError()
    pParent.left = pleft
    pParent.right = pright

def PrintTree(pRoot):
    print(pRoot.value)
    if (pRoot.left != None):
        PrintTree(pRoot.left)
    else:
        print("left child is nullptr.")
    if (pRoot.right != None):
        PrintTree(pRoot.right)
    else:
        print("right child is nullptr.")


# def DestroyTree(pRoot):
#     if (pRoot.left != None):
#         print("del left")
#         DestroyTree(pRoot.left)
#     if (pRoot.right != None):
#         print("del right")
#         DestroyTree(pRoot.right)
#
#     del pRoot


if __name__ == "__main__":
    pRoot = CreateBinaryTreeNode(1)
    pNode1 = CreateBinaryTreeNode(2)
    pNode2 = CreateBinaryTreeNode(3)
    ConnectTreeNodes(pRoot, pNode1, pNode2)
    PrintTree(pRoot)
    # DestroyTree(pRoot)
    # del pRoot
    # print(pRoot)
    # print(gc.collect())
    #
    # PrintTree(pRoot)
