class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BigHeap(object):
    def __init__(self, vals):
        head = self.init_tree(vals, 0, 1)
        head = self.heap_init(head)

    def heap_init(self, phead: TreeNode):
        if phead.left == None and phead.right == None:
            return
        if phead.left != None:
            self.heap_init(phead.left)

        if phead.left.val > phead.val:
            phead.left.val, phead.val = phead.val, phead.left.val

        if phead.right != None:
            self.heap_init(phead.right)

        if phead.right.val > phead.val:
            phead.right.val, phead.val = phead.val, phead.right.val





    def init_tree(self, vals, ptr, t):
        if ptr >= len(vals):
            return None
        if vals[ptr] != '#':
            head = TreeNode(vals[ptr])
            head.left = self.init_tree(vals, ptr+pow(2, ptr-1), t+1)
            head.right = self.init_tree(vals, ptr+pow(2, ptr-1)+1, t+1)
        else:
            return None
        return head

