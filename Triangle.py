# Problem: https://leetcode.com/problems/triangle/description/
# Multiple ways of solving this problem.
# Most elegant: O(n) space, bottom-up, triangle not modified
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # O(1) Space, Top-down DP, In-place
        
        if not triangle:
            return None
        
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                else:
                    triangle[i][j] = min(triangle[i][j] + triangle[i-1][j], \
                                         triangle[i][j] + triangle[i-1][j-1])                
        return min(triangle[-1])
