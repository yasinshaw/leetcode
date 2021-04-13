#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        mapt = {}
        for i in range(len(s)):
            if s[i] in map and t[i] not in mapt:
                return False
            if s[i] not in map and t[i] in mapt:
                return False
            if s[i] in map and t[i] in mapt and map[s[i]] != mapt[t[i]]:
                return False
            map[s[i]] = i
            mapt[t[i]] = i
        return True
# @lc code=end

