
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode: ListNode):
        lst = []
        while listNode.next != None:
            lst.append(listNode.val)
            listNode = listNode.next
        lst.append(listNode.val)
        lst = lst[:: -1]
        return lst
