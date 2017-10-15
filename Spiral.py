# Problem: https://leetcode.com/problems/spiral-matrix-ii/description/
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        if n == 0:
            return []
        
        res = [[0]*n for _ in xrange(n)]
        
        cnt = 1
        for k in xrange(n/2):
            for i in xrange(0+k, n-k):
                res[k][i] = cnt
                cnt += 1
            for i in xrange(1+k, n-k):
                res[i][n-1-k] = cnt
                cnt += 1
            for i in xrange(n-2-k, 0+k-1, -1):
                res[n-1-k][i] = cnt
                cnt += 1
            for i in xrange(n-2-k, 0+k, -1):
                res[i][0+k] = cnt
                cnt += 1
        if n%2 == 1:
            res[n/2][n/2] = cnt
        return res
