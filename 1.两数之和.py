#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        j=-1
        for i in range(lens):
            if (target - nums[i]) in nums:
                if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                    continue
                else:
                    j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2                
                    break
        if j>0:
            return [i,j]
        else:
            return []

        
# @lc code=end

