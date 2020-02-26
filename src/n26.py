from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        slow = 0
        fast = 0
        while fast < n:
            while fast < n -1 and nums[fast] == nums[fast + 1]:
                fast += 1
            nums[slow] = nums[fast]
            fast += 1
            slow += 1
        return slow
