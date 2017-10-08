# Problem: https://leetcode.com/problems/word-break/description/
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        bools = [False] * (len(s)+1)
        bools[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if (bools[j] and s[j:i] in wordDict):
                    bools[i] = True
                    break
        return bools[-1]
