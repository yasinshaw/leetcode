from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in map:
                return [map[another_num], index]
            map[num] = index
        return []
