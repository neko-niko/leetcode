class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False
        else:
            return self.panduan(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                           pRoot2)

    def panduan(self, p1, p2):
        if not p2:
            return True
        else:
            if not p1 or p1.val != p2.val:
                return False
            return self.panduan(p1.right, p2.right) and self.panduan(p1.left, p2.left)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.left = node2
    test1 = node1
    test2 = node2
    test1 = test1.left
    print(test1 == test2)
