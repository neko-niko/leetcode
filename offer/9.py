# // 面试题9：用两个栈实现队列
# // 题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail
# // 和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。
from queue import LifoQueue

class MyQueue(object):
    def __init__(self):
        self.queue = {1:LifoQueue(), 2:LifoQueue()}
        self.queue_ptr = 1
        self.lable = None
    def push(self, value):
        if self.lable == None or self.lable == 'push':
            pass
        else:
            while not self.queue[self.queue_ptr].empty():
                self.queue[3 - self.queue_ptr].put(self.queue[self.queue_ptr].get())
            self.queue_ptr = 3 - self.queue_ptr
            self.lable = 'push'
        self.queue[self.lable].put(value)

    def get(self):
        if self.lable == None or self.lable == 'push':
            while not self.queue[self.queue_ptr].empty():
                self.queue[3 - self.queue_ptr].put(self.queue[self.queue_ptr].get())
            self.queue_ptr = 3 - self.queue_ptr
            self.lable = 'get'
        else:
            pass
        if not self.queue[self.queue_ptr].empty():
            return self.queue[self.queue_ptr].get()
        else:
            return None
# if __name__ == "__main__":
