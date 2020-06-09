# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        head = ListNode(0)
        ptr = head
        while l1 and l2:
            temp = l1.val + l2.val + flag
            if temp >= 10:
                flag = 1
                temp = temp % 10
            else:
                flag = 0
            ptr.next = ListNode(temp)
            ptr = ptr.next
            l1, l2 = l1.next, l2.next
        # ptr.next = (l1 if l2 == None else l2) if flag == 0 else (ListNode(1) if l1 is None and l2 is None else (l1 if l2 == None else l2))
        if flag == 0:
            ptr.next = (l1 if l2 is None else l2)
        else:
            cur = l1 if l2 is None else l2
            while flag and cur:
                flag = (cur.val + flag) // 10
                ptr.next = ListNode(0) if flag else ListNode(cur.val + 1)
                ptr = ptr.next
                cur = cur.next
            ptr.next = (ListNode(0) if flag else None) if cur is None else cur
            if ptr.next and flag:
                ptr.next.val += 1
            # if cur is None:
            #     ptr.next = ListNode(1)

        return head.next


