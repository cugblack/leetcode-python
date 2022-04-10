# coding: utf8

class Node:
    # 初始化节点，仅包含k\v，前后指针为空
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        #
        self.prev = None
        self.next = None


class LRUCache:
    # 最新数据存储在头部
    # 
    def __init__(self, capacity):

        # 最大容量
        self.capacity = capacity

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        # key=key，value=node
        self.cache = dict()

        # 当前容量
        self.size = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        # move to head
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        # 更新/插入数据，从头部插入
        # 初始化节点
        node = Node(key, value)
        # 头节点表示最近使用的key
        if key not in self.cache:
            # 加入缓存字典、插入链表表头、长度+1
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1

            # 如果达到最大容量，触发淘汰机制
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        self.cache[key] = node
        self.moveToHead(node)
        return "OK"

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def get_all_keys(self):
        return self.cache.keys()


class LRUCacheNew:
    # 最新数据存储在尾部
    def __init__(self, capacity):
        self.capacity = capacity

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = dict()
        self.size = 0

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.moveToTail(node)
        return node.value

    def put(self, key, value):
        # 更新/插入数据，从尾部插入
        # 初始化节点
        node = Node(key, value)
        # 头节点表示最近使用的key
        if key not in self.cache:
            # 加入缓存字典、插入链表表头、长度+1
            self.cache[key] = node
            self.addToTail(node)
            self.size += 1

            # 如果达到最大容量，触发淘汰机制
            if self.size > self.capacity:
                removed = self.removeHead()
                self.cache.pop(removed.key)
                self.size -= 1
        self.cache[key] = node
        self.moveToTail(node)
        return "OK"

    def addToTail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def removeHead(self):
        node = self.head.next
        self.removeNode(node)
        return node

    def moveToTail(self, node):
        self.removeNode(node)
        self.addToTail(node)

    def get_all_keys(self):
        return self.cache.keys()


def test_lru_1():
    cache = LRUCache(capacity=3)
    cache.put("name1", "black1")
    cache.put("name2", "black2")
    cache.put("name3", "black3")

    print(cache.get("name"))
    print(cache.get("name1"))
    cache.put("name4", "black4")
    cache.put("name5", "black5")
    print(cache.get("name1"))
    cache.put("name6", "black6")
    print(cache.get("name1"))
    print(cache.get_all_keys())


def test_lru_2():
    cache = LRUCacheNew(capacity=4)
    cache.put("name1", "black1")
    cache.put("name2", "black2")
    cache.put("name3", "black3")

    print(cache.get("name"))
    print(cache.get("name1"))
    cache.put("name4", "black4")
    cache.put("name5", "black5")
    print(cache.get("name1"))
    cache.put("name6", "black6")
    print(cache.get("name1"))
    print(cache.get_all_keys())


if __name__ == "__main__":
    print("start 1---------")
    test_lru_1()
    print("start 2---------")
    test_lru_2()
