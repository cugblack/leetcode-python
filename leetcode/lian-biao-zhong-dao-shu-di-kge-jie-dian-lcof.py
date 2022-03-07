# 剑指 Offer 22. 链表中倒数第k个节点
# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode(), k: int) -> ListNode:

        former, later = head, head

        for _ in range(k):
            former = former.next
        while former:
            former, later = former.next, later.next
        return later


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    k = 2
    test = Solution()
    print(test.getKthFromEnd(l, k))
