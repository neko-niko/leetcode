class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        ptr = head
        if head == None:
            return None
        if k != 0:
            for i in range(k-1):  # K过大
                head = head.next
                if head == None:
                    return None
        if k == 0:
            return None
        while head.next != None:
            ptr = ptr.next
            head = head.next
        return ptr



