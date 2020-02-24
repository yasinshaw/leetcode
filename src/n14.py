from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        first_str = strs[0]
        n = len(first_str)
        has_common = True
        for i, c in enumerate(first_str):
            if has_common:
                for s in strs:
                    if i >= len(s) or s[i] != c:
                        has_common = False
                        break
                if has_common:
                    res += c
        return res