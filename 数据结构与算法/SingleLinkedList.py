class SingleLinkedList(object):
    """
    单链表
    """
    class SingleNode(object):
        """
        初始化节点
        """
        def __init__(self, item):
            self.value = item
            self.next = None

    def __init__(self, item=None):
        """
        初始化链表
        """
        if not item:
            self.__head = None
        else:
            node = self.SingleNode(item)
            node.next = self.__head
            self.__head = node
    
    def is_empty(self):
        """
        判断链表是否为空
        """
        return self.__head == None
    
    def length(self):
        """
        输出链表长度
        """
        count = 0
        current = self.__head
        while current != None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        """
        搜索元素
        """
        current = self.__head
        while current != None:
            if current.value == item:
                return True
            else:
                current = current.next
        return False

    def travel(self):
        """
        输出全部元素
        """
        current = self.__head
        print('start output: [', end=' ')
        while current != None:
            print(current.value, end=' ')
            current = current.next
        print('] end out.')

    def add(self, item):
        """
        头部插入节点
        """
        node = self.SingleNode(item)
        node.next = self.__head
        self.__head = node
    
    def append(self, item):
        """
        尾部追加元素
        """
        if self.is_empty():
            self.add(item)
        else:
            node = self.SingleNode(item)
            current = self.__head
            while current.next:
                current = current.next
            
            current.next = node
    
    def insert(self, idx, item):
        """
        指定位置插入节点
        """
        if idx <= 0:
            self.add(item)
        elif idx >= self.length():
            self.append(item)
        else:
            node = self.SingleNode(item)
            current = self.__head
            count = 0
            while count < idx - 1:
                current = current.next
                count += 1
            node.next = current.next
            current.next = node
    
    def remove(self, item):
        """
        删除元素
        """
        current = self.__head
        prev = None
        while current != None:
            if current.value != item:
                prev = current
                current = current.next
            else:
                if not prev:
                    """删除头节点"""
                    self.__head = current.next
                else:
                    """删除非头节点"""
                    prev.next = current.next
                return self.travel()
                

if __name__ == '__main__':

    s1 = SingleLinkedList()
    print(s1.is_empty())
    s1.add(5)
    s1.add(3)
    s1.add(1)
    s1.travel()
    print(s1.length())
    s1.append(7)
    s1.append(9)
    s1.travel()
    print(s1.insert(3, 8))
    s1.travel()
    s1.remove(9)
