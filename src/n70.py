class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        temp_one = 1
        temp_two = 2
        res = 0
        for x in range(3, n + 1):
            res = temp_one + temp_two
            temp_one = temp_two
            temp_two = res
        return res
