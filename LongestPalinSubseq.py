# Problem: https://leetcode.com/problems/longest-palindromic-subsequence/description/
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # so many tweaks !
        dp = [[0]*len(s) for i in xrange(len(s))]
        for i in xrange(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]
