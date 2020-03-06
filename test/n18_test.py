import unittest

from n18 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.fourSum([-3,-2,-1,0,0,1,2,3], 0), [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
        self.assertEqual(solution.fourSum([-1,0,1,2,-1,-4], -1), [[-4,0,1,2],[-1,-1,0,1]])
        self.assertEqual(solution.fourSum([0,0,0,0], 0), [[0,0,0,0]])


if __name__ == '__main__':
    unittest.main()
