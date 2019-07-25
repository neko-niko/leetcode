class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot is None:
            return []
        result = []
        result_ptr = 0
        result.append([])
        curr = 1
        next = 0
        queue = []
        queue.append(pRoot)
        while queue:
            node = queue.pop()
            curr -= 1
            if node.left:
                next += 1
                queue.insert(0, node.left)
            if node.right:
                next += 1
                queue.insert(0, node.right)
            result[result_ptr].append(node.val)
            if curr == 0:
                curr = next
                next = 0
                result_ptr += 1
                result.append([])
        result = result[: result_ptr]
        return result