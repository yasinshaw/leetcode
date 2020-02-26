from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        slow = 0
        fast = 0
        while fast < n:
            while fast < n and nums[fast] == val:
                fast += 1
            if fast < n:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return slow
