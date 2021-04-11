#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            mod = columnNumber % 26
            columnNumber = columnNumber // 26
            if mod == 0:
                res = 'Z' + res
                columnNumber -= 1
            else:
                # 65 is 'A'
                res = str(chr(65 + mod - 1)) + res
        return res
# @lc code=end

