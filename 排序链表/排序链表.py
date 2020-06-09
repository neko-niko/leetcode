# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        fast = slow = head
        pre = None
        if head is None or head.next is None:
            return head

        while fast is not None and fast.next is not None:
            pre = slow
            fast = fast.next.next
            slow = slow.next

        pre.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        if left.val <= right.val:
            result1 = result = left
            left = left.next
        else:
            result1 = result = right
            right = right.next

        while left and right:
            if left.val <= right.val:
                result.next = left
                left = left.next
            else:
                result.next = right
                right = right.next

        result.next = left if right is None else right
        return result1
