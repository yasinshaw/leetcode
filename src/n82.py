#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        sentinel = ListNode(0)
        pre = sentinel
        cur = head
        # 只要发现重复，就跳到下一个数字，否则，就加入链表
        while cur:
            pre.next = None
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                continue
            else:
                pre.next = cur
            if cur:
                pre = cur
                cur = cur.next
        return sentinel.next
                
# @lc code=end

