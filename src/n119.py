#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        prev = self.getRow(rowIndex - 1)
        result = [1]
        for i in range(len(prev)):
            if i == len(prev) - 1:
                break
            result.append(prev[i] + prev[i + 1])
        result.append(1)
        return result
# @lc code=end

