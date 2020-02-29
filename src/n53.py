from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = sum = nums[0]
        for i in range(1, n):
            if sum > 0:
                sum += nums[i]
            else:
                sum = nums[i]
            res = max(sum, res)
        return res
