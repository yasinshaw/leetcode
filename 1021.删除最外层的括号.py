#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        stack = [] 
        for c in S:
            if c == '(':
                if stack:
                    res.append(c)
                stack.append(c)
            if c == ')':
                stack.pop()
                if stack:
                    res.append(c)
        return "".join(res)
        
# @lc code=end

