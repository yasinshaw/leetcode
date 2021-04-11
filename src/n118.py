#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]] 
        if numRows == 2:
            return [[1], [1, 1]] 
        temp = self.generate(numRows - 1)
        prev = temp[numRows - 2]
        result = [1]
        for i in range(len(prev)):
            if i == len(prev) - 1:
                break
            result.append(prev[i] + prev[i + 1])
        result.append(1)
        temp.append(result)
        return temp


# @lc code=end

