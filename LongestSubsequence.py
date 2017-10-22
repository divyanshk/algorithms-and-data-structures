# Problem: https://leetcode.com/problems/longest-increasing-subsequence/description/    
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n2) solution
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in xrange(1, len(nums)):
            for j in xrange(0, i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j] + 1
        return max(dp)
