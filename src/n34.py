from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        first_pos = self._find_first_pos(nums, target)
        if first_pos == -1:
            return [-1, -1]
        last_pos = self._find_last_pos(nums, target)
        return [first_pos, last_pos]

    def _find_first_pos(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1

    def _find_last_pos(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left + 1) >> 1)
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return left
