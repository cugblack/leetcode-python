class LinkedListNode:
    """
    Init a node
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    """
    Single LinkedList with head
    """

    def __init__(self):
        """
        Init a empty LinkedList
        """
        self.head = LinkedListNode(value=None)
        self.head.next = None

    def is_empty(self):
        """
        Determine if LinkedList is empty
        """
        if self.head.next is None:
            return True
        return False

    def length(self):
        """
        Length of LinkedList
        """
        cur = self.head
        x = 0
        while cur.next:
            x += 1
            cur = cur.next
        return x

    def search(self, value):
        """
        Determine if value in LinkedList
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
        Return all node
        """
        cur = self.head
        while cur.next:
            cur = cur.next
            print(cur.value)

    def add(self, value):
        """
        Add node from head
        """
        node = LinkedListNode(value=value)
        node.next = self.head.next
        self.head.next = node

    def append(self, value):
        """
        Add node from tail
        """
        node = LinkedListNode(value=value)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert(self, idx, value):
        """
        Add node by index
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
        """
        Remove node by value
        """
        cur = self.head
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    s1 = SingleLinkedList()
    print(s1.is_empty())
    s1.add(5)
    s1.add(3)
    s1.add(1)
    s1.add(6)
    s1.append(2)
    s1.travel()
    print("length：", s1.length())
    s1.append(7)
    s1.append(9)
    s1.travel()
    print(s1.remove(6))
    s1.insert(3, 8)
    s1.travel()
