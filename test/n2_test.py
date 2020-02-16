import unittest

from n2 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_should_return_807_given_342_add_465(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)

    def test_should_return_81_given_81_add_0(self):
        l1 = ListNode(1)
        l1.next = ListNode(8)
        l2 = ListNode(0)
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 8)


if __name__ == '__main__':
    unittest.main()
