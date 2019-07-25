# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
import functools

import collections

Piar = collections.namedtuple('Piar', ['key', 'value'])
target = collections.namedtuple('target', [])


class MyHashMap(object):
    def __init__(self, total):
        self.total = total * 3
        self.main_lst = [None for _ in range(self.total)]
        self.cot = 0
        self.max = total

    def get(self, key):
        hash_key = key % self.total
        result = self.main_lst[hash_key]
        if not result:
            return -1
        elif result.key == key:
            return result.value
        else:
            return self.get_conflict_hand(key, hash_key+1)



    def get_conflict_hand(self, key, hash_key):
        if hash_key >= self.total:
            hash_key = 0        #环形缓冲区

        result = self.main_lst[hash_key+1]
        if not result:
            return -1
        elif result.key == key:
            return result.value
        else:
            return self.get_conflict_hand(key, hash_key+1)


    def insert(self, key, value):
        if self.cot >= self.max:
            

    def elimination(self):      #LRU淘汰
        pass


# class LRUCache:
#
#     def __init__(self, capacity: int):
#
#     def get(self, key: int) -> int:
#
#     def put(self, key: int, value: int) -> None:

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node(object):

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_map = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        if node.next != None:
            if node.prev == None:
                # head
                self.head = self.head.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.node_map:
            self.node_map[key].val = value
            self.get(key)
            return
        if len(self.node_map) == self.capacity:
            node = self.node_map[self.head.key]
            del self.node_map[self.head.key]
            self.node_map[key] = node
            node.val = value
            node.key = key
            self.get(key)
        else:
            node = Node(key, value)
            self.node_map[key] = node
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node


class MyLRUCache(object):
    def __init__(self, capacity: int):
        self.max_len = capacity
        self.hash_map = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.hash_map: return -1
        else:
            cur_node = self.hash_map[key]
            if cur_node.next:
                if cur_node.prev:
                    cur_node.next.prev = cur_node.prev
                    cur_node.prev.next = cur_node.next
                else:
                    self.head = cur_node.next
                    cur_node.next.prev = None
                self.tail.next = cur_node
                cur_node.prev = self.tail
                self.tail = cur_node
                self.tail.next = None
            return cur_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].val = value
            self.get(key)
        else:
            if len(self.hash_map) >= self.max_len:
                delete_node = self.head
                del self.hash_map[delete_node.key]
                delete_node.val = value
                delete_node.key = key
                self.hash_map[key] = delete_node
                self.get(key)
            else:
                cur_node = Node(key, value)
                self.hash_map[key] = cur_node
                if not self.head:
                    self.head = self.tail = cur_node
                else:
                    self.tail.next = cur_node
                    cur_node.prev = self.tail
                    self.tail = cur_node



