#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.getHight(root.left) - self.getHight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def getHight(self, root: TreeNode) -> int:
        if not root:
            return 0;
        return max(self.getHight(root.left), self.getHight(root.right)) + 1;
# @lc code=end

