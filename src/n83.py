from common.Structure import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        low = head
        fast = head.next
        while fast:
            while fast and fast.val == low.val:
                fast = fast.next
            low.next = fast
            low = fast
            if fast:
                fast = fast.next
        return head
