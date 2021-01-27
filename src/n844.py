#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#
import operator

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1, s2 = list(), list()
        for x in S:
            if x == '#' and s1:
                s1.pop()
            elif x != '#':
                s1.append(x)
        for y in T:
            if y == '#' and s2:
                s2.pop()
            elif y != '#':
                s2.append(y)
        return operator.eq(s1, s2)
        
# @lc code=end

