#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        newStr = s + s
        return s in newStr[1:-1]
        # def canRepeat(s, sub) -> bool:
        #     subLen = len(sub)
        #     k = 0 # 在subLen中的指针
        #     for i in range(subLen, len(s)):
        #         if s[i] != sub[k]:
        #             return False
        #         k = (k + 1) % subLen
        #     return k == 0

        # n = len(s)
        # first = s[0]
        # for i in range(1, len(s)):
        #     if s[i] == first:
        #         print(s[0:i])
        #         if canRepeat(s, s[0: i]):
        #             return True
        # return False

# @lc code=end

