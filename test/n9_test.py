import unittest

from n9 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.isPalindrome(121), True)
        self.assertEqual(solution.isPalindrome(-121), False)
        self.assertEqual(solution.isPalindrome(10), False)


if __name__ == '__main__':
    unittest.main()
