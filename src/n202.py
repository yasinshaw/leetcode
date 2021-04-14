#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        ## 求下一个数
        def getNext(n):
            res = 0
            while n > 0:
                mod = n % 10
                res += mod * mod
                n = n // 10
            return res
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = getNext(n)
        return n == 1


# @lc code=end

