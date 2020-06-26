class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        inner_cache = set()
        left = head
        right = head.next

        inner_cache.add(left.val)

        while right:
            if right.val in inner_cache:
                left.next = right.next
                right = right.next
            else:
                inner_cache.add(right.val)
                left = left.next
                right = right.next

        return head
