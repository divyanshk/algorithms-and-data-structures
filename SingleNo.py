#Problem: https://leetcode.com/problems/single-number/description/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        for i in xrange(len(nums)):
           t ^= nums[i]
        return t
