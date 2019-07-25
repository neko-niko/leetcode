# 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        result = self.judge(pRoot.left, pRoot.right)
        return result

    def judge(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            result = self.judge(left.right, right.left) and self.judge(left.left, right.right)
            result = result and left.val == right.val
            return result

    def In_order1(self, pRoot, lst):
        if pRoot is None:
            lst.append('#')
        else:
            self.In_order1(pRoot.left, lst)
            lst.append(pRoot.val)
            self.In_order1(pRoot.right, lst)

    def In_order2(self, pRoot, lst):
        if pRoot is None:
            lst.append('#')
        else:
            self.In_order2(pRoot.right, lst)
            lst.append(pRoot.val)
            self.In_order2(pRoot.left, lst)