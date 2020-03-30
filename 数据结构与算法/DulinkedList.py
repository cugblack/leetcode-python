class Node(object):
    def __init__(self, item):
        self.value = item
        self.next = None
        self.prev = None

class DuLinkedList(object):
    """
    双向链表
    """

    def __init__(self):
        self.__head = None

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
        头部增加元素
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
    
    def append(self, item):
        """
        尾部追加元素
        """
        if self.is_empty():
            self.add(item)
        else:
            node = Node(item)
            current = self.__head
            while current.next != None:
                current = current.next
            current.next = node
            node.prev = current

    def insert(self, idx, item):
        """
        指定位置插入
        """
        if idx <=0:
            self.add(item)
        elif  idx >= self.length():
            self.append(item)
        else:
            node = Node(item)
            current = self.__head
            i = 0
            while i < idx -1:
                current = current.next
                i += 1
            node.prev = current
            node.next = current.next
            current.next.prev = node
            current.next = node
    
    def remove(self, item):
        """
        删除元素
        """
        current = self.__head
        if current.value == item:
            if current.next:
                self.__head = current.next
            else:
                self.__head = None
            return
        
        while current != None:
            if current.value == item:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return self.travel()
            current = current.next
            

if __name__ == '__main__':

    s1 = DuLinkedList()
    print(s1.is_empty())
    s1.add(5)
    s1.add(3)
    s1.add(1)
    s1.travel()
    print(s1.length())
    s1.append(7)
    s1.append(9)
    s1.travel()
    s1.insert(3, 8)
    s1.travel()
    s1.remove(9)