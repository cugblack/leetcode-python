class Queue(object):
    """
    队列是一种特殊的线性表,是一种先进先出（FIFO）的数据结构
    只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作
    进行插入操作的端称为队尾，进行删除操作的端称为队头
    队列中没有元素时，称为空队列
    """
    def __init__(self):
        """
        初始化队列
        """
        self.__items = []
    
    def is_empty(self):
        """
        判断队列是否为空
        """
        return self.length() == 0
    
    def length(self):
        """
        队列长度
        """
        return len(self.__items)


    def enqueue(self, item):
        """
        入队
        """
        self.__items.append(item)
    
    def dequeue(self):
        """
        出队
        """
        return self.__items.pop(0)

def josephus_problem(namelist, num):
    """
    约瑟夫问题
    """
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.length() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()
    


if __name__ == '__main__':
    name_list = ['cug', 'black', 'hei', 'edwin', 'one', 'plu']
    print(josephus_problem(name_list, 1))