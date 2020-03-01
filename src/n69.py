class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        cur = x // 2
        while True:
            pre = cur
            cur = (cur + x // cur) // 2
            if cur * cur <= x < (cur + 1) * (cur + 1):
                return cur
