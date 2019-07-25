# // 面试题7：重建二叉树
# // 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输
# // 入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,
# // 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，则重建出
# // 图2.6所示的二叉树并输出它的头结点。
from Utilities.BinaryTree import *

def Construct(prologue, medium, pro_start, pro_end, mid_start, mid_end):
    value = prologue[pro_start]
    pRoot = CreateBinaryTreeNode(value)

    if pro_start == pro_end:
        if mid_end == mid_start and prologue[pro_start] == medium[mid_start]:
            return pRoot


    i = mid_start
    while medium[i] != value:       #从中序遍历中找到根节点的值
        i += 1
    left_length = i - mid_start
    print("length = ", left_length, "end-start=", pro_end - pro_start)
    if left_length > 0:
        pRoot.left = Construct(prologue, medium, pro_start + 1, pro_start + left_length, mid_start, i - 1)

    if left_length < pro_end - pro_start:
        pRoot.right = Construct(prologue, medium, pro_start + left_length + 1, pro_end, i + 1, mid_end)
    return pRoot

if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    mid = [4, 7, 2, 1, 5, 3, 8, 6]
    # try:
    #     tree_root = Construct(pre, mid, 0, len(pre) - 1, 0, len(mid) - 1)
    # except:
    #     pass
    tree_root = Construct(pre, mid, 0, len(pre) - 1, 0, len(mid) - 1)
    PrintTree(tree_root)