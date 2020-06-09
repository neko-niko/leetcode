class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead: ListNode):
        slow = pHead.next
        if slow is None:
            return None
        fast = slow.next
        if fast is None:
            return None
        while fast is not None and slow is not None:
            if fast == slow:
                meetnode = fast
                break
            fast = fast.next
            slow = slow.next
            if fast != slow:
                fast = fast.next
        else:
            return None
        cot = 1
        beifen1 = meetnode
        while beifen1.next != meetnode:
            beifen1 = beifen1.next
            cot += 1
        fast = pHead
        slow = pHead
        for _ in range(cot):
            fast = fast.next

        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

