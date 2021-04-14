#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ## 用原数组来存这个信息
        n = len(nums)
        res = []
        for x in nums:
            # 这样比较好处理x为n的情况
            temp = (x - 1) % n
            nums[temp] += n
        for i, v in enumerate(nums):
            if v <= n:
                res.append(i + 1)
        return res
# @lc code=end

