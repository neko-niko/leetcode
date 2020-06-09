class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        if root is None:
            return ''
        result = []
        self.SerializeCore(root, result)
        return '-'.join(result)

    def SerializeCore(self, node, result_lst):
        if node is None:
            result_lst.append('#')
        else:
            result_lst.append(node.val)
            self.SerializeCore(node.left, result_lst)
            self.SerializeCore(node.right, result_lst)

    def Deserialize(self, s):
        if s == '':
            return None
        else:
            lst = s.split('-')
            return self.DeserializeCore(lst)
    def DeserializeCore(self, lst):
        if lst[0] == '#':
            lst.remove(0)
            return None
        else:
            node = TreeNode(int(lst.remove(0)))
            if lst:
                node.left = self.DeserializeCore(lst)
            if lst:
                node.right = self.DeserializeCore(lst)
            return node