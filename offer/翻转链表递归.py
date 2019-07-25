class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def ReversedList(self, head: ListNode):
        if head is None or head.next is None:
            return head
        else:
            newhead = self.ReversedList(head.next)
            head.next.next = head
            head.next = None
            return newhead
