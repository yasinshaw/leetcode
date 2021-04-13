#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
# 维护一个滑动窗口，[i, j]， i <= j。
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res = []
        i = 0 
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j + 1] == nums[j] + 1:
                j += 1
            if j == i:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[j]))
            i = j + 1
        return res
# @lc code=end

