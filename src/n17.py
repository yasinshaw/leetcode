from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        if n == 0:
            return res
        hash_map = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def dfs(temp: str, index: int):
            if index == n:
                res.append(temp)
                return
            char = digits[index]
            string = hash_map[char]
            for c in string:
                dfs(temp + c, index + 1)
        dfs("", 0)
        return res
