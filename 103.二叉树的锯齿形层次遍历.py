#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        left_to_right = True
        while queue:
            cur_res = []
            cur_len = len(queue)
            if left_to_right:
                for i in range(0, cur_len, 1):
                    cur = queue.popleft()
                    cur_res.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            else:
                for i in range(cur_len, 0, -1):
                    cur = queue.pop()
                    cur_res.append(cur.val)
                    if cur.right:
                        queue.appendleft(cur.right)
                    if cur.left:
                        queue.appendleft(cur.left)
            left_to_right = not left_to_right
            res.append(cur_res)
        return res
    
# @lc code=end

