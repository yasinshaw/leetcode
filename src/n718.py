#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# 先理解题目，第一时间可以想到的是滑动窗口，和递归（动态规划）。两个都是比较优秀的算法，可以都写一遍
# @lc code=start
class Solution:
    # 动态规划
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j]标识nums1[i]与nums2[j]为起始位置的最长公共子数组的长度
        n, m = len(nums1), len(nums2)
        # 初始化为0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                ans = max(ans, dp[i][j])
        return ans

    # 暴力，复杂的n^3
    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        for i in range(nums1):
            for j in range(nums2):
                k = 0
                # 这里有重复计算
                while nums1[i] == nums2[j]:
                    k += 1
                result = max(result, k)
        return result



# @lc code=end

