class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre: list, tin: list):
        if pre == [] or tin == []:
            return None
        if len(pre) == 1:
            node = TreeNode(pre[0])
            return node
        val = pre[0]
        node = TreeNode(val)
        find_tin = 0
        while tin[find_tin] != val:
            find_tin += 1
            if find_tin >= len(pre):
                return None
        left_len = find_tin
        node.left = self.reConstructBinaryTree(pre=pre[1:1 + left_len], tin=tin[:find_tin])
        node.right = self.reConstructBinaryTree(pre=pre[1 + left_len:], tin=tin[find_tin + 1:])
        return node

if __name__ == '__main__':
    # lst = [1, 2, 3]
    pass
#     # print(lst[1:2])