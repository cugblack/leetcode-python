# 206. 反转链表
# https://leetcode-cn.com/problems/reverse-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_1(head: ListNode) -> ListNode:
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


def reverse_list_2(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    cur = reverse_list_2(head.next)
    head.next.next = head
    head.next = None
    return cur
