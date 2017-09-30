# Problem: https://leetcode.com/problems/search-for-a-range/description/
# Solution: Using two binary search,
#           being lazy, so using bisect
import bisect
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        else:
            return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)-1]
