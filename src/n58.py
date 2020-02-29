class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                if count == 0:
                    continue
                else:
                    break
            else:
                count += 1
        return count
