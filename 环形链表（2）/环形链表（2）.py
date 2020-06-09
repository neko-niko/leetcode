# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回
# null。
#
# 为了表示给定链表中的环，我们使用整数
# pos
# 来表示链表尾连接到链表中的位置（索引从
# 0
# 开始）。 如果
# pos
# 是 - 1，则在该链表中没有环。
#
# 说明：不允许修改给定的链表。
#
#
#
# 示例
# 1：
#
# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：tail
# connects
# to
# node
# index
# 1
# 解释：链表中有一个环，其尾部连接到第二个节点。


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        else:
            ptr1 = head
            ptr2 = ptr1.next
            while ptr1 is not None and ptr2 is not None:
                if ptr1 == ptr2:
                    meetnode = ptr1
                    break
                else:
                    ptr2 = ptr2.next
                    ptr1 = ptr1.next
                    if ptr1 != ptr2 and ptr2 is not None:
                        ptr2 = ptr2.next

            else:
                return None

            cot = 1
            tempnode = meetnode.next
            while tempnode != meetnode:
                tempnode = tempnode.next
                cot += 1

            ptr1 = ptr2 = head
            for i in range(cot):
                ptr2 = ptr2.next

            while ptr2 != ptr1:
                ptr2 = ptr2.next
                ptr1 = ptr1.next
            return ptr1
