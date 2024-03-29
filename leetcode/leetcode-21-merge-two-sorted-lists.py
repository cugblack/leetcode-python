# 21. 合并两个有序链表
# https://leetcode-cn.com/problems/merge-two-sorted-lists/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    prev_head = ListNode()
    prev = prev_head
    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next
    prev.next = list1 if list1 is not None else list2
    return prev_head.next


def merge_two_lists_2(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    elif not list2:
        return list1
    elif list1.val < list2.val:
        list1.next = merge_two_lists_2(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_2(list2.next, list1)
        return list2
