#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        k = k % n
        if k == 0:
            return head
        count = 0
        cur = head
        pre = cur
        while count < n - k:
            count += 1
            pre = cur
            cur = cur.next
        pre.next = None
        newHead = cur
        while cur.next:
            cur = cur.next
        cur.next = head
        return newHead

# @lc code=end

