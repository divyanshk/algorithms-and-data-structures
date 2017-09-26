# Problem: https://leetcode.com/problems/palindrome-partitioning/description/
class Solution(object):
    def isPalin(self, s, pos1, pos2):
        return (s[pos1:pos2+1] == s[pos1:pos2+1][::-1])
    
    def backtrack(self, s, pos, res, templist):
        if (pos == len(s)):
            res.append(templist[:])
            return
        for i in xrange(pos, len(s)):
            if (self.isPalin(s, pos, i)):
                templist.append(s[pos:i+1])
                self.backtrack(s, i+1, res, templist)
                templist.pop()
            
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        templist = []
        self.backtrack(s, 0, res, templist)
        return res
