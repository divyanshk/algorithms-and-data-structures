# Problem: https://leetcode.com/problems/decode-ways/description/
class Solution(object):    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = map(int, list(s))
        dp = [0] * (len(s)+1)
        dp[0]=0
        inValid = False
        if s[0] == 0:
            return 0
        dp[1] += 1
        if len(s) == 1:
            return dp[1]
        if s[1] in xrange(0, 7) and s[0] == 2:
                dp[2] += 1
        elif s[1] in xrange(0, 10) and s[0] == 1:
                dp[2] += 1
        if s[1] is not 0:
            dp[2] += 1
        
        for i in xrange(3, len(s)+1):
            if s[i-1] in xrange(0, 7) and s[i-2] == 2:
                dp[i] += dp[i-2]
            elif s[i-1] in xrange(0, 10) and s[i-2] == 1:
                dp[i] += dp[i-2]
            if s[i-1] is not 0:
                dp[i] += dp[i-1]
            elif s[i-2] not in xrange(1,3):
                inValid = True
                break
        return 0 if inValid else dp[-1]
