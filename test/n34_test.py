import unittest

from n34 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])


if __name__ == '__main__':
    unittest.main()
