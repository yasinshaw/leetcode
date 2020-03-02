import unittest

from n8 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.myAtoi("123"), 123)
        self.assertEqual(solution.myAtoi(" -123"), -123)
        self.assertEqual(solution.myAtoi(" +123sss"), 123)
        self.assertEqual(solution.myAtoi(" +123 4"), 123)
        self.assertEqual(solution.myAtoi("  2147483648"), 2147483647)
        self.assertEqual(solution.myAtoi("  -2147483649"), -2147483648)
        self.assertEqual(solution.myAtoi("  "), 0)
        self.assertEqual(solution.myAtoi("  ss"), 0)
        self.assertEqual(solution.myAtoi("  +ss"), 0)
        self.assertEqual(solution.myAtoi("s123"), 0)
        self.assertEqual(solution.myAtoi(" +-123sss"), 0)
        self.assertEqual(solution.myAtoi(" --123sss"), 0)


if __name__ == '__main__':
    unittest.main()
