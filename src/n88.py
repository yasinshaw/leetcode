from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length = m + n
        i = m - 1
        j = n - 1
        for k in range(length - 1, -1, -1):
            if j < 0:
                return
            if i < 0 or nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
