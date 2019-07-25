class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root: TreeNode):
        lst = []
        out = []
        if not root:
            return []
        lst.append(root)
        for i in lst:
            out.append(i.val)
            if i.left != None:
                lst.append(i.left)
            if i.right != None:
                lst.append(i.right)
        return out


if __name__ == '__main__':
    pass

