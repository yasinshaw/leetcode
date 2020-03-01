from common.Structure import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        low = head
        fast = head.next
        while fast is not None:
            while fast is not None and fast.val == low.val:
                fast = fast.next
            low.next = fast
            low = fast
            if fast is not None:
                fast = fast.next
        return head
