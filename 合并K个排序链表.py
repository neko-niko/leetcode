# Definition for singly-linked list.

# 两种思路：
# 1.建立最小堆（更简单的可以败者树）, 每次取最小值用时log(n),总元素个数假设为m, 则总用时为小于mlog(n)(n为要合并链表个数)
# 2.每次取两个list排序, 当只剩两个list事对剩下的两个排序得到结果, 依此递归， 时间复杂度同上
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list):     #排序解法  使用自带的min函数和index替换速度很慢
        while True:
            try:
                lists.remove(None)
            except:
                break

        try:
            lists[0]
        except:
            return []

        lst = [i for i in lists]
        head = min(lst, key=lambda x: x.val)

        if head.next:
            lst[lst.index(head)] = head.next
        else:
            lst.remove(head)


        cur_node = head

        while len(lst) != 0:
            min_node = min(lst, key=lambda x: x.val)
            cur_node.next = min_node
            if min_node.next:
                lst[lst.index(min_node)] = min_node.next
            else:
                lst.remove(min_node)
            cur_node = cur_node.next

        return head


    def mergeKLists2(self, lists: list):
        lst_len = len(lists)
        if lst_len == 2:
            return self.two_list_merge(lists[0], lists[1])
        if lst_len == 1:
            return lists[0]

        midd = lst_len // 2
        lst1 = lists[0: midd]
        lst2 = lists[midd: ]


        return self.two_list_merge(self.mergeKLists2(lst1), self.mergeKLists2(lst2))





    def two_list_merge(self, phead1: ListNode, phead2: ListNode):
        if phead1 is None:
            return phead2
        if phead2 is None:
            return phead1

        if phead1.val < phead2.val:
            head = phead1
            head.next = self.two_list_merge(phead1.next, phead2)
        else:
            head = phead2
            head.next = self.two_list_merge(phead1, phead2.next)
        return head


if __name__ == '__main__':
    pass
