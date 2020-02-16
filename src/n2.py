from common.Structure import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = False
        result = ListNode(0)
        head = result
        while l1 is not None or l2 is not None:
            while l1 is None and l2 is not None:
                sum, carry = self.__compute_sum_and_carry(0, l2.val, carry)
                l2 = l2.next
                result.next = ListNode(sum)
                result = result.next
            while l2 is None and l1 is not None:
                sum, carry = self.__compute_sum_and_carry(l1.val, 0, carry)
                l1 = l1.next
                result.next = ListNode(sum)
                result = result.next
            if l1 is None and l2 is None:
                break
            sum, carry = self.__compute_sum_and_carry(l1.val, l2.val, carry)
            l1 = l1.next
            l2 = l2.next
            result.next = ListNode(sum)
            result = result.next
        if carry:
            result.next = ListNode(1)
        return head.next

    def __compute_sum_and_carry(self, val1, val2, carry):
        sum = val1 + val2 + carry
        if sum >= 10:
            carry = True
            sum %= 10
        else:
            carry = False
        return sum, carry
