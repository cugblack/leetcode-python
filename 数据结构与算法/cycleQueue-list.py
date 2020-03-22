class CycleQueue(object):
    """
    数组实现循环队列
    """
    def __init__(self, size):
        self.max_size = size + 1
        self.__head = 0
        self.__tail = 0
        self.__items = [None] * self.max_size
    
    def is_empty(self):
        """
        判断队列是否为空
        """
        return self.__head == self.__tail
    
    def is_full(self):
        """
        判断对列是否已满
        """
        return (self.__tail + 1) % self.max_size == self.__head

    def length(self):
        """
        队列长度
        """
        return (self.__tail - self.__head + self.max_size) % self.max_size

    def enqueue(self, item):
        """
        入队
        """
        if self.is_full():
            return False
        self.__items[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.max_size
        return True

    def dequeue(self):
        """
        出队
        """
        if self.is_empty():
            return False

        data = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__head = (self.__head + 1) % self.max_size
        return data 

    def clear(self):
        """
        清空队列
        """
        self.__head = 0
        self.__tail = 0
        self.__items = [None] * self.max_size
        return True
    
    def list_queue(self):
        return self.__items

if __name__ == '__main__':
    q = CycleQueue(4)
    # 测试用例
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    print("队列元素：", q.list_queue())
    print("是否队满: ", q.is_full())
    print(q.dequeue())
    q.enqueue(9)
    print("队列元素：", q.list_queue())
    print(q.length())

    print(q.dequeue())
    q.enqueue(3)
    print("队列元素：", q.list_queue())
    print(q.length())
    q.clear()
    print("队列元素：", q.list_queue())
    q.length()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    print("队列元素：", q.list_queue())