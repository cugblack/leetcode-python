# 2. 两数相加
# https://leetcode-cn.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_nums(l1: ListNode, l2: ListNode) -> ListNode:
    head = curr = ListNode(0)
    carry = 0
    val = 0

    while l1 or l2:
        x, y = 0, 0
        if l1:
            l1, x = l1.next, l1.val
        if l2:
            l2, y = l2.next, l2.val
        s = x + y + carry
        carry = s // 10
        curr.next = ListNode(s % 10)
        curr = curr.next
    if carry > 0:
        curr.next = ListNode(1)
    return head.next



