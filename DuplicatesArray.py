# Problem: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            else:
                res.append(abs(nums[i]))
        return res
