import unittest

from n14 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(solution.longestCommonPrefix(["dog", "racecar", "car"]), "")
        self.assertEqual(solution.longestCommonPrefix(["aa", "a"]), "a")


if __name__ == '__main__':
    unittest.main()
