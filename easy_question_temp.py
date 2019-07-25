from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def deleteNode(self, node: ListNode):
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            node = None



if __name__ == '__main__':
    print(2 ^ 3)
