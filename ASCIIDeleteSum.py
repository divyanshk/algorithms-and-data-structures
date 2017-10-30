# Problem: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
class Solution(object):
    def minimumDeleteSum(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        if not word1 and not word2:
            return 0
        dp = [[0]*(len(word2)+1) for _ in xrange(len(word1)+1)]
        
        for i in xrange(1, len(word1)+1):
            dp[i][0] = dp[i-1][0] + ord(word1[i-1])
        
        for i in xrange(1, len(word2)+1):
            dp[0][i] = dp[0][i-1] + ord(word2[i-1])
            
        for i in xrange(1, len(word1)+1):
            for j in xrange(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(word1[i-1]),\
                                       dp[i][j-1] + ord(word2[j-1])) 
                    
        return dp[len(word1)][len(word2)]
