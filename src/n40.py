#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=star
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target: int, begin: int, path: List[int], res: List[List[int]]):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            numSet = set()
            for i in range(begin, len(candidates)):
                if candidates[i] in numSet:
                    continue
                else:
                    numSet.add(candidates[i])
                    dfs(target - candidates[i], i + 1, path + [candidates[i]], res)
        path = []
        res = []
        dfs(target, 0, path, res)
        return res
# @lc code=end

