import unittest

from n1 import *


class MyTestCase(unittest.TestCase):
    solution = Solution()

    def test_something(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4], 5), [1, 2])
        self.assertEqual(self.solution.twoSum([1, 3, 5, 6], 6), [0, 2])


if __name__ == '__main__':
    unittest.main()
