import unittest

from n6 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.convert("LEETCODEISHIRING", 3), "LCIRETOESIIGEDHN")
        self.assertEqual(solution.convert("LEETCODEISHIRING", 4), "LDREOEIIECIHNTSG")


if __name__ == '__main__':
    unittest.main()
