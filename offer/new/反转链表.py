# 输入一个链表，反转链表后，输出新链表的表头。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead: ListNode):
        if pHead == None:
            return None
        else:
            left = None
            right = pHead
            while right.next != None:
                tmp = right
                right = right.next
                tmp.next = left
                left = tmp
        right.next = left
        return right
