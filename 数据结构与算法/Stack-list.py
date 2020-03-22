class Stack(object):
    """
    数组实现栈
    """
    def __init__(self):
        """
        初始化为空栈
        """
        self.__items = []
    
    def is_empty(self):
        """
        判断栈是否为空
        """
        return self.__items == []
    
    def length(self):
        """
        栈的长度
        """
        return len(self.__items)
    
    def push(self, item):
        """
        入栈
        """
        self.__items.append(item)
    
    def pop(self):
        return self.__items.pop(self.length() -1)

    def clear(self):
        del self.__items[:]

if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(0)
    stack.push(1)
    stack.push(0)
    stack.push(1)
    print(stack.pop())
    print(stack.length())
    stack.clear()
    print(stack.length())