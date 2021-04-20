#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from heapq import *

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for x in nums:
            if x in map:
                map[x] += 1
            else:
                map[x] = 1
        # 然后用堆，python没有自带的最大堆，所以这里先不写了。。
 
        
# @lc code=end

