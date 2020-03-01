import unittest

from n69 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.mySqrt(4), 2)


if __name__ == '__main__':
    unittest.main()
