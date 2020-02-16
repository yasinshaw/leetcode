from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in number_map:
                return [number_map[another_num], index]
            number_map[num] = index
        return []
