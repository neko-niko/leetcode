class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.min = 1e10
    def push(self, node):
        if node < self.min:
            self.min = node
        self.stack1.append(node)
        self.stack2.append(self.min)
    def pop(self):
        self.stack2.pop()
        return self.stack1.pop()
    def top(self):
        return self.stack1[-1]
    def min(self):
        return self.stack2[-1]


