from common.Structure import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0) # 倒数第n + 1个
        pre.next = head
        res = pre
        tail = head # 倒数第1个结点
        for i in range(0, n):
            tail = tail.next
        while tail:
            tail = tail.next
            pre = pre.next
        pre.next = pre.next.next
        return res.next
