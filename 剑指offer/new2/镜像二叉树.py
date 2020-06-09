class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return None
        else:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root