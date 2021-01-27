#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        dict = {}
        stack = list()
        for x in nums2:
            while stack and x > stack[-1]:
                dict[stack.pop()] = x
            stack.append(x) 
        for i in range(len(nums1)):
            if nums1[i] in dict:
                res[i] = dict[nums1[i]]
        return res

        
# @lc code=end

