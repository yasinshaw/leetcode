#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nStr = str(n)
        nums = []
        for x in nStr:
            nums.append(int(x))
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            return -1
        self.nextPermutation(nums)
        strs = []
        for x in nums:
            strs.append(str(x))
        res = int("".join(strs))
        return res if (res >= 1 and res <= (2**31) - 1) else -1
        

    # 参考31号题目，下一个排列
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j > 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# @lc code=end

