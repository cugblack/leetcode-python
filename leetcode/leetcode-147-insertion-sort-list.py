# 147. 对链表进行插入排序
# https://leetcode-cn.com/problems/insertion-sort-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertion_sort_list(head: ListNode) -> ListNode:
    """
    思路：
        按照插入排序的思路，分别记录已排序空间和未排序空间；
        每次在未排序空间取一个数，分别和已排序空间的节点迭代
    步骤如下：
        1、引入tmp作为临时节点指向头结点
        2、last_sorted作为有序空间的最后一个节点
        3、cur为未排序空间的第一个节点
        4、每次对比cur.next和last_sorted的值，如果cur.next更大，则迭代last_sorted
        5、否则进行插入：
            利用prev从有序空间的头开始;
            和cur.next的值比较;
            直到找到大于cur.next的节点prev.next
        6、插入：
            last_sorted的下一个节点为cur.next;
            cur.next指向prev.next;
            prev.next = cur
        7、结束本次循环，cur = last_sorted.next
        8、重复循环
    """
    if not head:
        return head
    tmp = ListNode(0)
    tmp.next = head
    last_sorted = head
    cur = head.next

    while cur:
        if last_sorted.val <= cur.val:
            last_sorted = last_sorted.next
        else:
            prev = tmp

            while prev.next.val <= cur.val:
                prev = prev.next

            last_sorted.next = cur.next
            cur.next = prev.next
            prev.next = cur

        cur = last_sorted.next

    return tmp.next
