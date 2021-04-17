#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 回溯。定义一个递归函数，在[k, n - 1]找子集
        def dfs(nums: List[int], path: List[int], result: List[List[int]], k: int):
            result.append(path.copy())
            for i in range(k, len(nums)):
                newPath = path + [nums[i]]
                dfs(nums, newPath, result, i + 1)
                newPath.pop()
        dfs(nums, [], result, 0)
        return result
# @lc code=end

