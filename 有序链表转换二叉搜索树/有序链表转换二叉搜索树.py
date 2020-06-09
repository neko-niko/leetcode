# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #
        # def findmid(head: ListNode, tail: ListNode):
        #     fast = head
        #     slow = head
        #     while fast != tail and fast.next != tail:
        #         slow = slow.next
        #         fast = fast.next.next
        #
        #     return slow
        #
        # def helper(head: ListNode, tail: ListNode) ->  TreeNode:
        #     if head == tail:
        #         return
        #     else:
        #         mid = findmid(head, tail)
        #         temp = TreeNode(mid.val)
        #         temp.right = helper(mid.next, tail)
        #         temp.left = helper(head, mid)
        #         return temp
        # return helper(head, None)
        if not head: return None
        elif not head.next: return TreeNode(head.val)
        else:
            fast = slow = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            tmp = slow.next
            slow.next = None    #断尾
            res = TreeNode(slow.val)
            res.left = self.sortedListToBST(head)
            res.right = self.sortedListToBST(tmp)
            return res

