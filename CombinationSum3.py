# Problem: https://leetcode.com/problems/combination-sum-iii/description/
class Solution(object):
    def combinationSum3Util(self, lis, sum, res, k, n):
        if k == 0 and sum == n:
          res.append(lis[:])
          return
        start = 1 if len(lis) == 0 else lis[-1]+1
        for i in xrange(start, 10):
            if i+sum<=n:
                lis.append(i)
                self.combinationSum3Util(lis, (i+sum), res, k-1, n)
                lis.pop()
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.combinationSum3Util([], 0, res, k, n)
        return res
