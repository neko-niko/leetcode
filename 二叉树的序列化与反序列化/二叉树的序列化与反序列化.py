from queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        res = []
        def dfs(root):
            if root is None:
                res.append(None)
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return str(res)


    def deserialize(self, data: str) -> TreeNode:
        serialize_lst = eval(data)
        if not serialize_lst:
            return None

        def helper(l: list):
            if not l:
                return None
            elif l[0] is None:
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = helper(l)
            root.right = helper(l)
            return root

        return helper(serialize_lst)




if __name__ == '__main__':
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node2 = node1.right = TreeNode(3)
    node2.left = TreeNode(4)
    node2.right = TreeNode(5)
    temp = Codec().serialize(node1)
    print(temp)
    root = Codec().deserialize(temp)
    print(Codec().serialize(root))
