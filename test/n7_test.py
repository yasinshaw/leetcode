import unittest

from n7 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.reverse(321), 123)
        self.assertEqual(solution.reverse(-321), -123)
        self.assertEqual(solution.reverse(2147483647), 0)


if __name__ == '__main__':
    unittest.main()
