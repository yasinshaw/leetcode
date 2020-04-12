from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(str, left, right):
            """
            深度优先遍历
            :param str: 目前的字符串
            :param left: 左括号剩余个数
            :param right: 右括号剩余个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(str)
                return
            if right < left:
                return
            if left > 0:
                dfs(str + "(", left - 1, right)
            if right > 0:
                dfs(str + ")", left, right - 1)

        dfs('', n, n)
        return res
