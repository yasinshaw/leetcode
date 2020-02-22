class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x > 0 else -1
        x = abs(x)
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if (rev > 2147483647 // 10) or (rev == 2147483647 // 10 and pop > 7):
                return 0
            rev = rev * 10 + pop
        return flag * rev