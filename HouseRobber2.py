# Problem: https://leetcode.com/problems/house-robber-ii/description/
class Solution(object):
    def robSimple(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in xrange(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robSimple(nums[:-1]), self.robSimple(nums[1:]))
