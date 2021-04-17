#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 这个地方用max，因为会比较多个j
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

