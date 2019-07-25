import functools
class ListNode(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


def CreateListNode(value, next = None):
    pNode = ListNode(value, next)
    return pNode

def ConnectListNode(node1, node2):
    node1.next = node2

def PrintList(node):
    print(node.value)
    if node.next != None:
        PrintList(node.next)


if __name__ == "__main__":
    nodelist = [CreateListNode(i)for i in range(10)]
    for i in range(len(nodelist) - 1):
        ConnectListNode(nodelist[i], nodelist[i+1])
    PrintList(nodelist[0])
