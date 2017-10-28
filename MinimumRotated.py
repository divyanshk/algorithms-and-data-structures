# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print id(nums)
        lo = 0
        hi = len(nums)-1
        
        if lo == hi:
            return nums[lo]
        
        if hi - lo == 1:
            return nums[hi] if nums[hi] < nums[lo] else nums[lo]
        
        mid = lo + (hi - lo)/2
        
        if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
            return nums[mid]
        
        elif nums[mid] > nums[mid+1]:
            return nums[mid+1]
        
        if nums[mid] < nums[hi]:
            hi = mid-1
        elif nums[mid] > nums[hi]:
            lo = mid + 1
        
        return self.findMin(nums[lo:hi+1])
