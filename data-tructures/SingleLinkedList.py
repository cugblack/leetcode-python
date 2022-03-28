class LinkedListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    """
    单链表 带头节点
    """

    def __init__(self):
        """
        初始化 空节点
        """
        self.head = LinkedListNode(value=None)
        self.head.next = None

    def is_empty(self):
        """
        判断： 链表是否为空
        """
        if self.head.next is None:
            return True
        return False

    def length(self):
        """
        查询： 链表长度
        """
        cur = self.head
        x = 0
        while cur.next:
            x += 1
            cur = cur.next
        return x

    def search(self, value):
        """
        查找： 任意元素
        """
        cur = self.head
        while cur.next:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        return False

    def travel(self):
        """
        查询：返回链表全部元素
        """
        cur = self.head
        while cur.next:
            cur = cur.next
            print(cur.value)

    def add(self, value):
        """
        插入： 从头部插入
        """
        node = LinkedListNode(value=value)
        node.next = self.head.next
        self.head.next = node

    def append(self, value):
        """
        插入： 从尾部追加
        """
        node = LinkedListNode(value=value)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert(self, idx, value):
        """
        插入： 从指定位置插入
        """
        node = LinkedListNode(value)
        cur = self.head
        index = 1
        while index < idx:
            cur = cur.next
            index += 1

        node.next = cur.next
        cur.next = node

    def remove(self, value):
        cur = self.head
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
                return True
            else:
                cur = cur.next
        return False

    def reverse(self):
        # TO DO
        pass


if __name__ == '__main__':
    s1 = SingleLinkedList()
    print(s1.is_empty())
    s1.add(5)
    s1.add(3)
    s1.add(1)
    s1.add(6)
    s1.append(2)
    s1.travel()
    print("长度：", s1.length())
    s1.append(7)
    s1.append(9)
    s1.travel()
    print(s1.remove(6))
    s1.insert(3, 8)
    s1.travel()
