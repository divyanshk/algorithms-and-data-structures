# Problem: https://leetcode.com/problems/rotate-image/description/
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in xrange(n/2):
            for i in xrange(j, n-1-j):
                temp = matrix[j][i]
                matrix[j][i] = matrix[n-1-i][j]
                matrix[n-1-i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = matrix[i][n-1-j]
                matrix[i][n-1-j] = temp
