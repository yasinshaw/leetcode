#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 用二分法，时间换空间来满足题目额外要求
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            count = 0
            for x in nums:
                if x < mid:
                    count += 1
            if count >= mid:
                right = mid - 1
            else:
                left = mid
        return left

# @lc code=end

