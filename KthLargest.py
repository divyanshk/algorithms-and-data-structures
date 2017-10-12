# Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
from random import randint
class Solution(object):
    def partition(self, nums, lo, hi, p):
        # partition in descending order
        nums[p], nums[hi] = nums[hi], nums[p]
        i = lo - 1
        for j in xrange(lo, hi):
            if nums[j] > nums[hi]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[hi] = nums[hi], nums[i+1]
        return i+1
            
    def findKthLargestUtil(self, nums, k, lo, hi):
        if lo >= hi:
            return nums[lo]
        p = randint(lo, hi)
        p = self.partition(nums, lo, hi, p)
        if p == k:
            return nums[k]
        elif p < k:
            return self.findKthLargestUtil(nums, k, p+1, hi)
        else:
            return self.findKthLargestUtil(nums, k, lo, p-1)
            
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # randomised quickselect => expected linear time
        # median of medians => worst case linear time
        
        return self.findKthLargestUtil(nums, k-1, 0, len(nums)-1)
