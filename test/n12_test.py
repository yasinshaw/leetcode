import unittest

from n12 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.intToRoman(3), "III")
        self.assertEqual(solution.intToRoman(4), "IV")
        self.assertEqual(solution.intToRoman(9), "IX")
        self.assertEqual(solution.intToRoman(58), "LVIII")
        self.assertEqual(solution.intToRoman(1994), "MCMXCIV")


if __name__ == '__main__':
    unittest.main()
