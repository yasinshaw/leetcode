import unittest

from n3 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_should_return_3_given_abcabcbb(self):
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_should_return_1_given_bbbbb(self):
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_should_return_3_given_pwwkew(self):
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_should_return_1_given_s(self):
        self.assertEqual(solution.lengthOfLongestSubstring("s"), 1)


if __name__ == '__main__':
    unittest.main()
