import unittest

from n58 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.lengthOfLastWord("Hello World"), 5)


if __name__ == '__main__':
    unittest.main()
