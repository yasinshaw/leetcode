#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for s in arr:
            if s == "..":
                if stack:
                    stack.pop()
            elif s and s != ".":
                stack.append(s)
        return "/" + "/".join(stack)
        
# @lc code=end

