# // 面试题6：从尾到头打印链表
# // 题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
import queue
from Utilities import List

def PrintListReverse(link_head):
    stack = queue.LifoQueue()
    while link_head != None:
        stack.put(link_head.value)
        link_head = link_head.next

    # stack.put(link_head.value)

    while stack.empty() != True:
        print(stack.get())


if __name__ == "__main__":
    nodelist = []
    for i in range(10):
        nodelist.append(List.CreateListNode(i))

    for i in range(9):
        List.ConnectListNode(nodelist[i], nodelist[i + 1])
    # List.ConnectListNode(nodelist[-1], nodelist[0])

    PrintListReverse(nodelist[0])

