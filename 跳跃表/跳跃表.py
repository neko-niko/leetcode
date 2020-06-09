import random


class SkipListNode(object):
    def __init__(self, key: object, value: object):
        self.key = key
        self.value = value
        self.forward = []


class SkipList(object):
    def __init__(self, max_level: int):
        self.max_level = max_level
        self.header = self.createnode(0, 0)
        self.header.forward = [None] * (max_level - 1)
        self.level = 0

    @staticmethod
    def createnode(key: object, value: object) -> SkipListNode:
        temp_node = SkipListNode(key, value)
        return temp_node

    def randomlevel(self) -> int:
        k = 1
        while random.random() <= 0.5:
            k += 1
        return k if k <= self.max_level else self.max_level

    def insert(self, key: object, value: object) -> bool:
        q = None
        p = self.header
        k = self.level
        update = [None] * self.max_level
        for i in reversed(range(k)):

            q = p.forward[i]
            while q is not None and q.key < key:
                p = q
                q = p.forward[i]
            update[i] = p

        if q and q.key == key:
            return False

        # 产生随机数k
        # 新建待插入节点q
        # 一层层插入
        k = self.randomlevel()
        if k > self.level:
            for i in range(self.level, k):
                update[i] = self.header
            self.level = k
        q = self.createnode(key, value)
        for i in range(0, k):
            q.forward.append(update[i].forward[i])
            update[i].forward[i] = q
        return True

    def delete(self, key: object) -> bool:
        update = [None] * self.max_level
        p, q = self.header, None
        k = self.level
        for i in reversed(range(k)):
            q = p.forward[i]
            while q and q.key < key:
                p = q
                q = q.forward[i]

            update[i] = p

        if q and q.key == key:
            for i in range(0, self.level):
                if update[i].forward[i] == q:
                    update[i].forward[i] = q.forward[i]

            for i in reversed(range(0, self.level)):
                if self.header.forward[i] is None:
                    self.level -= 1
            return True
        else:
            return False

    def find(self, key: object):
        p, q = self.header, None

        k = self.level
        for i in reversed(range(0, k)):
            q = p.forward[i]
            while q and q.key <= key:
                if q.key == key:
                    return q.value
                p = q
                q = q.forward[i]

if __name__ == '__main__':
    sl = SkipList(5)
    print(sl.insert(1, 2))
    print(sl.insert(2, 2))
    print(sl.insert(3, 1))
    print(sl.insert(1, 2))
    temp = sl.header
    while temp:
        print(temp.key)
        temp = temp.forward[2]

    print(sl.find(10))