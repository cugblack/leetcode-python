
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组
        """
        prenode = ListNode(0)
        lastnode = prenode
        val = 0
        while val or l1 or l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next


a = ListNode([1,2,3])
b = ListNode([902])
print(Solution().addTwoNumbers(a,b))