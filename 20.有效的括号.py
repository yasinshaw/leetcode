#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack  = list()
        pair = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for char in s:
            if char not in pair:
                if not stack or pair[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return not stack

# @lc code=end

