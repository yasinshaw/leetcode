#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []
        i, j = 0, len(numbers) - 1
        while i < j:
            temp = numbers[i] + numbers[j]
            if temp == target:
                return [i + 1, j + 1]
            if temp < target:
                i += 1
            if temp > target:
                j -= 1
        return []

# @lc code=end

