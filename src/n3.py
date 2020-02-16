class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = -1
        map = {}
        for i, char in enumerate(s):
            left = max(left, map.get(char, -1))
            res = max(res, i - left)
            map[char] = i
        return res
