import unittest
from typing import List

from common.Structure import build_list
from n21 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        l1 = build_list([1, 2, 4])
        l2 = build_list([1, 3, 4])
        res = build_list([1, 1, 2, 3, 4, 4])
        expected = solution.mergeTwoLists(l1, l2)
        self.assertEqual(expected, res)



if __name__ == '__main__':
    unittest.main()
