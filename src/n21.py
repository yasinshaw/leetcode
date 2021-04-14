# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common.Structure import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode(0)
        cur = sentinel
        while l1 is not None or l2 is not None:
            if l1 is None:
                cur.next = l2
                break
            if l2 is None:
                cur.next = l1
                break
            if l1.val <= l2.val:
                cur.next = l1
            else:
                cur.next = l2
            cur = cur.next
        return sentinel.next

        # head = ListNode(0)
        # temp = head
        # while l1 is not None or l2 is not None:
        #     if l2 is None or (l1 is not None and l1.val <= l2.val):
        #         temp.next = l1
        #         l1 = l1.next
        #     else:
        #         temp.next = l2
        #         l2 = l2.next
        #     temp = temp.next
        # return head.next
