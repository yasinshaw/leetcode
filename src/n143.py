#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        # 找链表中间结点，如果是奇数个，slow得超过一半才行
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 后半部分反转链表
        reversedHead = self.reverse(slow.next)
        slow.next = None
        # 合并两个链表
        curLeft, curRight = head, reversedHead
        while curLeft and curRight:
            tempLeft = curLeft.next
            tempRight = curRight.next
            curLeft.next = curRight
            curRight.next = tempLeft
            curLeft = tempLeft
            curRight = tempRight
    
    def reverse(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
            
# @lc code=end

