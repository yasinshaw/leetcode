import unittest

from n13 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.romanToInt("III"), 3)
        self.assertEqual(solution.romanToInt("IV"), 4)
        self.assertEqual(solution.romanToInt("IX"), 9)
        self.assertEqual(solution.romanToInt("LVIII"), 58)


if __name__ == '__main__':
    unittest.main()
