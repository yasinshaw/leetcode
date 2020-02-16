import unittest

from n1 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(solution.twoSum([1, 2, 3, 4], 5), [1, 2])
        self.assertEqual(solution.twoSum([1, 3, 5, 6], 6), [0, 2])


if __name__ == '__main__':
    unittest.main()
