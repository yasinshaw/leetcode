import unittest

from n20 import *

solution = Solution()


class MyTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.isValid("()"), True)
        self.assertEqual(solution.isValid("()[]{}"), True)
        self.assertEqual(solution.isValid("(]"), False)
        self.assertEqual(solution.isValid("([)]"), False)
        self.assertEqual(solution.isValid("{[]}"), True)


if __name__ == '__main__':
    unittest.main()
