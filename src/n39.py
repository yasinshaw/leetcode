#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target: int, begin: int, path: List[int], res: List[List[int]]):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(begin, len(candidates)):
                dfs(target - candidates[i], i, path + [candidates[i]], res)
        path = []
        res = []
        dfs(target, 0, path, res)
        return res
                
            
            
        

# @lc code=end

