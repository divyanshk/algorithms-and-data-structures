# Problem: https://leetcode.com/problems/find-peak-element/description/
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1  
        while (lo < hi):
            mid = (hi+lo)/2
            if (hi-lo) > 1:
                if (nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]):
                    return mid
                elif (nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]):
                    lo = mid + 1
                elif (nums[mid] < nums[mid-1] and nums[mid] > nums[mid+1]):
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # edge cases
                return hi if nums[hi]>nums[lo] else lo
        return lo
