class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        while pHead.next is not None and pHead.val == pHead.next.val:
            pHead = self.fuzhu1(pHead)

        ptr1 = pHead
        if ptr1 is None:
            return pHead
        ptr2 = ptr1.next
        if ptr2 is None:
            return pHead
        while ptr2.next is not None:
            if ptr2.next.val != ptr2.val:
                ptr2 = ptr2.next
                ptr1 = ptr1.next
            else:
                val = ptr2.val
                while ptr2 is not None and ptr2.val == val:
                    ptr2 = ptr2.next
                ptr1.next = ptr2
                if ptr2 is None:
                    break
        return pHead

    def fuzhu1(self, pHead):
        lable = 0
        while pHead.next is not None and pHead.val == pHead.next.val:
            pHead = pHead.next
            lable = 1
        if lable == 1:
            pHead = pHead.next
        return pHead

node1 = ListNode(1)
node2 = ListNode(1)
node1.next = node2
Solution().deleteDuplication(node1)