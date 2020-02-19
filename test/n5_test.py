import unittest

from n5 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.longestPalindrome("abcba"), "abcba")


if __name__ == '__main__':
    unittest.main()
