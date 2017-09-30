# Problem: https://leetcode.com/problems/permutations/description/
class Solution(object):
    def backtrack(self, nums, lo, hi, res):
        if (lo == hi):
            res.append(nums[:])
        else:
            for i in xrange(lo, hi+1):
                nums[i], nums[lo] = nums[lo], nums[i]
                self.backtrack(nums, lo+1, hi, res)
                nums[i], nums[lo] = nums[lo], nums[i]
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums:
            return []
        self.backtrack(nums, 0, len(nums)-1, res);
        return res
