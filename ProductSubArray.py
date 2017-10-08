# Problem: https://leetcode.com/problems/maximum-product-subarray/description/
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxpre = nums[0]
        minpre = nums[0]
        maxsofar = nums[0]
        for i in xrange(1, len(nums)):
            maxhere = max(max(nums[i]*maxpre, nums[i]*minpre), nums[i])
            minhere = min(min(nums[i]*maxpre, nums[i]*minpre), nums[i])
            maxsofar = max(maxhere, maxsofar)
            maxpre, minpre = maxhere, minhere
        return maxsofar
