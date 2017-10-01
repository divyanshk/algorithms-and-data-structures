# Problem: https://leetcode.com/problems/unique-binary-search-trees/description/
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in xrange(2, n+1):
            for t in xrange(1, i+1):
                dp[i] += dp[t-1] * dp[i-t]
        
        return dp[-1]
