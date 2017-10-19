# Problem: https://leetcode.com/problems/partition-equal-subset-sum/description/
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2 == 1:
            return False
        target = sum(nums)/2
        dp = [[False]*(target+1) for _ in xrange(len(nums)+1)]
        for i in xrange(len(nums)+1):
            dp[i][0] = True
        for j in xrange(target+1):
            dp[0][j] = False
        for i in xrange(1, len(nums)+1):
            for tar in xrange(1, target+1):
                if tar < nums[i-1]:
                    dp[i][tar] = dp[i-1][tar]
                else:
                    dp[i][tar] = dp[i-1][tar] or dp[i-1][tar-nums[i-1]]
        return dp[len(nums)][target]
