# Problem: https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2) solution
        if not nums:
            return 0
        dp = [1]*len(nums)
        trackNum = [1]*len(nums)
        maximumLength = 1
        for i in xrange(1, len(nums)):
            for j in xrange(0, i):
                if nums[j] < nums[i]:
                    if dp[i] == dp[j]+1:
                        trackNum[i] += trackNum[j]
                    elif dp[i] < dp[j]+1:
                        dp[i] = dp[j] + 1
                        trackNum[i] = trackNum[j]
                        maximumLength = dp[i] if maximumLength < dp[i] else maximumLength
                        
        return reduce(lambda i, j: i+j, \
                      map(lambda k: trackNum[k], \
                         filter(lambda i: dp[i] == maximumLength, xrange(len(dp)))))
