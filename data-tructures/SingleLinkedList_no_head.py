class LinkedListNode:
    """
    Init a node
    """

    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    """
    Single LinkedList, without head node
    """

    def __init__(self):
        """
        Init a empty LinkedList
        """
        self.head = None

    def is_empty(self):
        """
        Determine if LinkedList is empty
        """
        if self.head is None:
            print(self.head)
            return True
        return False

    def travel(self):
        """
        Return all node
        """
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

    def length(self):
        """
        Length of LinkedList
        """
        le = 0
        cur = self.head
        while cur:
            le += 1
            cur = cur.next
        return le

    def search(self, value):
        """
        Determine if value in LinkedList
        """
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        return False

    def add(self, value):
        """
        Add node from head
        """
        node = LinkedListNode(value=value)
        node.next = self.head
        self.head = node

    def append(self, value):
        """
        Add node from tail
        """
        node = LinkedListNode(value=value)
        cur = self.head
        if self.head is None:
            self.head = node
            self.head.next = None
        else:
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
        while index < idx-1:
            cur = cur.next
            index += 1

        node.next = cur.next
        cur.next = node

    def remove(self, value):
        """
        Remove node by value
        """
        cur = self.head
        if cur.value == value:
            self.head = cur.next
            return self.travel()
        else:
            while cur.next:
                if cur.next.value == value:
                    cur.next = cur.next.next
                    return self.travel()
                else:
                    cur = cur.next
            return -1


if __name__ == '__main__':
    s1 = SingleLinkedList()
    print(s1.is_empty())
    s1.travel()
    s1.append(6)
    s1.append(8)
    print(s1.search(5))
    print("length: ", s1.length())
    s1.add(3)
    s1.add(5)
    print(s1.search(5))
    s1.remove(8)
    s1.travel()
    print("length: ", s1.length())
    s1.insert(2, 4)
    s1.travel()
