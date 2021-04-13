#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        map = {}
        for i in range(0, n):
            if nums[i] in map and i - map[nums[i]] <= k:
                return True
            map[nums[i]] = i
        return False
# @lc code=end

