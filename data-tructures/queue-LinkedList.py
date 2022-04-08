class Node:
    """
    初始化链表节点
    """

    def __init__(self, value):
        self.value = value
        self.pre = None
        self.next = None


class LinkedList:
    """
    双向链表：带头尾节点
    """

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def is_empty(self):
        if self.head.next is None:
            return True
        return False

    def length(self):
        if self.is_empty():
            return 0
        length = 0
        cur = self.head.next
        while cur is not None and cur != self.tail:
            length += 1
            cur = cur.next
        return length

    # def add(self, value):
    #     node = Node(value=value)
    #     node.next = self.head.next
    #     node.pre = self.head
    #     self.head.next.pre = node
    #     self.head.next = node

    def append(self, value):
        node = Node(value=value)
        node.next = self.tail
        node.pre = self.head.pre
        self.tail.pre.next = node
        self.tail.pre = node

    def remove_head(self):
        self.head.next.next.pre = self.head
        self.head.next = self.head.next.next

    def travel(self):

        cur = self.head.next
        while cur is not None and cur != self.tail:
            print(cur.value)
            cur = cur.next
        return True


class Queue(object):
    """
    队列是一种特殊的线性表,是一种先进先出（FIFO）的数据结构
    只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作
    进行插入操作的端称为队尾，进行删除操作的端称为队头
    队列中没有元素时，称为空队列
    """

    def __init__(self):
        self.queue = LinkedList()

    def length(self):
        return self.queue.length()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.remove_head()

    def all_keys(self):
        self.queue.travel()


if __name__ == '__main__':
    # 测试用例
    q = Queue()
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(6)
    print("len:", q.length())
    q.dequeue()
    q.all_keys()
    print("len:", q.length())
    # l1 = LinkedList()
    # l1.add(1)
    # l1.add(3)
    # l1.add(5)
    # l1.append(6)
    # l1.travel()
    # print(l1.length())
