class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        for i in range(0, n - m + 1):
            k = i
            j = 0
            while j < m and k < n and haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == m:
                return i
        return -1
