#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# 经典的回溯法
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(nums: List[int], path: List[int]) -> None:
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i in nums:
                if i not in path:
                    path.append(i)
                    dfs(nums, path)
                    path.pop()
        dfs(nums, [])
        return result
                
            
# @lc code=end

