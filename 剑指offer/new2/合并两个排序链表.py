class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 == None and pHead2 == None:
            return None
        elif pHead2 == None or pHead1 == None:
            return (pHead2 if pHead1 == None else pHead1)
        else:
            if pHead1.val < pHead2.val:
                head = pHead1
                pHead1 = pHead1.next
            else:
                head = pHead2
                pHead2 = pHead2.next
            head2 = head
            while pHead2 != None and pHead1 != None:
                if pHead1.val < pHead2.val:
                    head.next = pHead1
                    pHead1 = pHead1.next
                    head = head.next
                else:
                    head.next = pHead2
                    pHead2 = pHead2.next
                    head = head.next
            curr = pHead1 if pHead2 == None else pHead2
            head.next = curr

        return head2

