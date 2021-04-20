#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 定义深度优先的函数，表示某节点下时候有p或者q中的其中一个
        self.result = root
        self.dfs(root, p, q)
        return self.result
    def dfs(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if not root:
            return False
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        # 满足以下条件，说明root就是最近公共祖先
        if (left and right) or ((left or right) and (root.val == p.val or root.val == q.val)):
            self.result = root
        return left or right or (root.val == p.val or root.val == q.val)
# @lc code=end

