import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                if math.fabs(target - sum) < math.fabs(target - res):
                    res = sum
                if sum == target:
                    return target
                elif sum < target:
                    L += 1
                else:
                    R -= 1
        return res
