import unittest

from n704 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_should_return_3_given_abcabcbb(self):
        self.assertEqual(solution.search([1, 2, 3, 4, 5], 4), 3)


if __name__ == '__main__':
    unittest.main()
